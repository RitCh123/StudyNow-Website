//for form validation
  function validateForm() {
    
    email = document.getElementById("email").value;

    password = document.getElementById("password").value;

    
    
    if (email != "" && password != "") {
      return true;
    } else {
      if (email == "") {
        document.getElementById('email').style.border = "1px solid #ff0000";
      }
      if (password == "") {
        document.getElementById('password').style.border = "1px solid #ff0000";
      }
    }
    return false;
  }
  

  
