var amountField = document.getElementById("amount")
var rateField = document.getElementById("rate")
var monthsField = document.getElementById("months")
var resultBox = document.getElementById("result")

amountField.addEventListener("input", calculate)
rateField.addEventListener("input", calculate)
monthsField.addEventListener("input", calculate)

function calculate(e) {
    amount = amountField.value
    rate = rateField.value
    months = monthsField.value
    if (amount != "" && rate != "" && months != "") {
        amount = Number(amount)
        rate = Number(rate)
        months = Number(months)
        monthlyPayment = ((amount + amount * (rate / 100)) / months).toFixed(2)
        resultBox.innerText = `Monthly Payment  = ${monthlyPayment}`
    }
    else {
        resultBox.innerText = ""
    }
}