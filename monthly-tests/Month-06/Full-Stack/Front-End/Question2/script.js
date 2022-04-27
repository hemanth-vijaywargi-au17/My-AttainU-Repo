let userField = document.getElementById('username')
let emailField = document.getElementById('email')
let pass1Field = document.getElementById('pass1')
let pass2Field = document.getElementById('pass2')

let submitBtn = document.getElementById('submit-btn')

let userMessageBox = document.getElementById('userMessage')
let emailMessageBox = document.getElementById('emailMessage')
let pass1MessageBox = document.getElementById('pass1Message')
let pass2MessageBox = document.getElementById('pass2Message')

submitBtn.addEventListener('click',()=>{
    let validUser = false
    let validEmail = false
    let validPass = false

    if(userField.value==""){
        userMessageBox.innerText = "Please Enter a Username"
        userMessageBox.style.color = "red"
        userField.style.borderColor = "red"
        validUser = false
    }
    else{
        userMessageBox.innerText = ""
        userMessageBox.style.color = ""
        userField.style.borderColor = "green"
        validUser = true
    }

    if(emailField.value==""){
        emailMessageBox.innerText = "Please Enter an Email"
        emailMessageBox.style.color = "red"
        emailField.style.borderColor = "red"
        validEmail = false
    }
    else{
        emailMessageBox.innerText = ""
        emailMessageBox.style.color = ""
        emailField.style.borderColor = "green"
        validEmail = true
    }

    if(pass1Field.value==""){
        pass1MessageBox.innerText = "Please Enter a Password"
        pass1MessageBox.style.color = "red"
        pass1Field.style.borderColor = "red"
    }

    if(pass2Field.value==""){
        pass2MessageBox.innerText = "Please Enter a Password"
        pass2MessageBox.style.color = "red"
        pass2Field.style.borderColor = "red"
        validPass = false
    }
    else if(pass1Field.value!=pass2Field.value){
        pass1MessageBox.innerText = "Passwords don't Match!"
        pass1MessageBox.style.color = "red"
        pass1Field.style.borderColor = "red"
        pass2MessageBox.innerText = "Passwords don't Match!"
        pass2MessageBox.style.color = "red"
        pass2Field.style.borderColor = "red"
        validPass = false
    }
    else{
        pass1MessageBox.innerText = ""
        pass1MessageBox.style.color = ""
        pass1Field.style.borderColor = "green"
        pass2MessageBox.innerText = ""
        pass2MessageBox.style.color = ""
        pass2Field.style.borderColor = "green"
        validPass = true
    }
    if(validEmail && validUser && validPass){
        console.log(
            {username:userField.value,
            email:emailField.value,
            password:pass1Field.value}
        )
    }
})