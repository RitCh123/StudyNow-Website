from Cryptodome.Cipher import AES

from Cryptodome import Random

from flask import Flask, render_template, request, session, redirect, url_for

import pymongo

import dns

#from documentation: 

#https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html





client = pymongo.MongoClient("mongodb+srv://Rit:studynow@studynow.rxugc.mongodb.net/studyNow?retryWrites=true&w=majority")
db = client.studyNow

users = db.users

app = Flask('app')

app.secret_key = "eeeb04b2d4ddc54a76d49e18"


@app.route('/')

def homePage():
  try:
    if session['username'] != "":
      return "Hello " + session['username']
  except Exception:
    return "Hello World!"

@app.route('/sign_in', methods = ["GET", "POST"])
def signIn():

  if request.method == "POST":
    email = request.form['email']

    password = request.form['password']

    

    if users.find_one({"email": email, "password": password}):
      session['email'] = email

      session['username'] = users.find_one({"email": email, "password": password})['username']

      return redirect(url_for("homePage"))
    

    


  return render_template("signIn/signIn.html")


@app.route('/sign_up', methods = ["GET", "POST"])

def signUp():
  
  if request.method == "POST":

    username = request.form['username']

    email = request.form['email']

    password = request.form['password']

    
    insertUser = {
      "username": username,
      "email": email,
      "password": password
    }

    users.insert_one(insertUser)

    session['username'] = username

    session['email'] = email

    return redirect(url_for("homePage"))

  return render_template("signUp/signUp.html")


#app.route('/')

app.run(host='0.0.0.0', port=8080, debug=True)