var inputField = document.getElementById("input")
var processBtn = document.getElementById("process")
var message1 = document.getElementById("message1")
var message2 = document.getElementById("message2")

processBtn.addEventListener("click", function () {
    input = inputField.value
    res = []
    del = []
    for (let i = 0; i < input.length; i++) {
        if (input[i] == "#") {
            if (res.length != 0) {
                del.push(res.pop())
            }
        }
        else {
            res.push(input[i])
        }
    }
    message1.innerText = "Processed String : " + res.join("")
    message2.innerText = "Deleted String : " + del.join("")
})