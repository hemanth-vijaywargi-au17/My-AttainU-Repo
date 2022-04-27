let numberBox = document.getElementById("numberBox")
let numberField = document.getElementById("cardNumber")

let nameBox = document.getElementById("nameBox")
let cardNameBox = document.getElementById("card-name")
let dateBox = document.getElementById("dateBox")
let monthBox = document.getElementById("monthBox")
let yearBox = document.getElementById("yearBox")

let nameField = document.getElementById("name")
let yearField = document.getElementById("year")
let monthField = document.getElementById("month")
let cvvField = document.getElementById("cvv")

let cardBox = document.getElementById("card-box")
let cardBox2 = document.getElementById("card-box2")
let whiteBar = document.getElementById("white-bar")

numberField.addEventListener("focusin", e => {
    numberBox.style.borderColor = "white"
})
numberField.addEventListener("focusout", e => {
    numberBox.style.borderColor = ""
})
numberField.addEventListener("input", e => {
    string = e.currentTarget.value
    numberField.value = string
    numberBox.innerText = string
})




nameField.addEventListener("focusin", e => {
    nameBox.style.borderColor = "white"

})

nameField.addEventListener("focusout", e => {
    nameBox.style.borderColor = ""
})
nameField.addEventListener("input", e => {
    cardNameBox.innerText = e.currentTarget.value.toUpperCase()
})



yearField.addEventListener("focusin", e => {
    dateBox.style.borderColor = "white"
})

yearField.addEventListener("focusout", e => {
    dateBox.style.borderColor = ""
})
yearField.addEventListener("input", e => {
    yearBox.innerText = yearField.value[2] + yearField.value[3]
})


monthField.addEventListener("focusin", e => {
    dateBox.style.borderColor = "white"
})

monthField.addEventListener("focusout", e => {
    dateBox.style.borderColor = ""
})
monthField.addEventListener("input", e => {
    monthBox.innerText = monthField.value
})

cvvField.addEventListener("focusin", e => {
    cardBox.style.transform = "rotateY(180deg)";
    cardBox2.style.transform = "rotateY(180deg)";
    cardBox2.style.zIndex = "1";
    cardBox.style.zIndex = "0";
})

cvvField.addEventListener("focusout", e => {
    cardBox.style.transform = "rotateY(0deg)";
    cardBox2.style.transform = "rotateY(0deg)";
    cardBox2.style.zIndex = "0";
    cardBox.style.zIndex = "1";
})

cvvField.addEventListener("input", e => {
    whiteBar.innerText = "*".repeat(e.currentTarget.value.length)
})