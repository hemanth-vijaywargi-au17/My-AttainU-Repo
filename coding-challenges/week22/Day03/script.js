var inputField = document.getElementById("number_field")
var warningBox = document.getElementById("warning")
var queueBox = document.getElementById("queue_box")
var add_btn = document.getElementById("add")
var remove_btn = document.getElementById("remove")

var queue = []

add_btn.addEventListener("click", function () {
    var value = inputField.value
    if (value != "") {
        warningBox.innerText = ""
        inputField.style.removeProperty('border');
        queue.push(value)
        queueBox.innerText = queue.join()
        inputField.value = ""
    }
    else {
        warningBox.innerText = "Please Enter a Number to Push"
        inputField.style.borderColor = "red"
    }
})

remove_btn.addEventListener("click", function () {
    if (queueBox.innerText == "") {
        warningBox.innerText = "Queue is Already Empty"
    }
    else {
        queue.shift()
        queueBox.innerText = queue.join()
    }
})
