var inputField = document.getElementById("number_field")
var warningBox = document.getElementById("warning")
var stackBox = document.getElementById("stack_box")
var push_btn = document.getElementById("push")
var pop_btn = document.getElementById("pop")

var stack = []

push_btn.addEventListener("click", function () {
    var value = inputField.value
    if (value != "") {
        warningBox.innerText = ""
        inputField.style.removeProperty('border');
        stack.push(value)
        stackBox.innerText = stack.join()
        inputField.value = ""
    }
    else {
        warningBox.innerText = "Please Enter a Number to Push"
        inputField.style.borderColor = "red"
    }
})

pop_btn.addEventListener("click", function () {
    if (stackBox.innerText == "") {
        warningBox.innerText = "Stack is Already Empty"
    }
    else {
        stack.pop()
        stackBox.innerText = stack.join()
    }
})
