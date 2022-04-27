let amountField = document.getElementById("amount")
let percentageField = document.getElementById("percentage")
let tipField = document.getElementById("tip")
let totalField = document.getElementById("total")
let calculateBtn = document.getElementById("calculate")

calculateBtn.addEventListener("click", calculate)

function calculate() {
    let amount = amountField.value
    let percentage = percentageField.value
    if (amount != "" && percentage != "") {
        amount = Number(amount)
        percentage = Number(percentage)
        tipAmount = amount * (percentage / 100)
        total = amount + tipAmount
        tipField.value = "$ " + tipAmount.toFixed(2)
        totalField.value = "$ " + total.toFixed(2)
    }
}

function clear() {
    tipField.value = ""
    totalField.value = ""
}

amountField.addEventListener("input", clear)
percentageField.addEventListener("input", clear)
