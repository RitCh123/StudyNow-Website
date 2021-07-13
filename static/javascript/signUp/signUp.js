//for form validation
  function validateForm() {
    
    username = document.getElementById("username").value;

    email = document.getElementById("email").value;

    password = document.getElementById("password").value;

    confirmPassword = document.getElementById("confirmPassword").value;

    checkbox = document.getElementById("checkbox").checked;

    
    
    if (username != "" && email != "" && password != "" && confirmPassword != "" && checkbox) {
      return true;
    } else {
      if (username == "") {
        document.getElementById('username').style.border = "1px solid #ff0000";  
      }
      if (email == "") {
        document.getElementById('email').style.border = "1px solid #ff0000";
      }
      if (password == "") {
        document.getElementById('password').style.border = "1px solid #ff0000";
      }
      if (confirmPassword == "") {
        document.getElementById('confirmPassword').style.border = "1px solid #ff0000";
      }
    
    }
    if (password != confirmPassword) {
      alert("hi")
      document.getElementById("smallWarning").style.display = "block";

      

      return false
      

      

    }
    return false;


    


    
  }
  

  
