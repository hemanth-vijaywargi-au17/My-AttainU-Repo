let cur1Field = document.getElementById("currency1")
let cur2Field = document.getElementById("currency2")
let cur1Select = document.getElementById("cur1Select")
let cur2Select = document.getElementById("cur2Select")
let swapBtn = document.getElementById("swap")
let infoBox = document.getElementById("info")

async function get() {
    let promiseObj = await fetch("http://api.exchangeratesapi.io/v1/latest?access_key=8636b3158abc20c94555e5384f44d229")
    let response = await promiseObj.json()
    let rates = response.rates
    getRates(rates)
}

function getRates(rates) {
    for (const key in rates) {
        if (key == "USD") {
            cur1Select.innerHTML += `<option selected value="${key}">${key}</option>`
        }
        else {
            cur1Select.innerHTML += `<option value="${key}">${key}</option>`
        }

        if (key == "INR") {
            cur2Select.innerHTML += `<option selected value="${key}">${key}</option>`
        }
        else {
            cur2Select.innerHTML += `<option value="${key}">${key}</option>`
        }

    }

    cur1Field.addEventListener("input", calculate)
    cur1Select.addEventListener("input", calculate)
    cur2Select.addEventListener("input", calculate)

    swapBtn.addEventListener("click", e => {
        let temp = cur1Select.value
        cur1Select.value = cur2Select.value
        cur2Select.value = temp
        calculate()
    })

    function calculate(e) {
        let cur1 = cur1Select.value
        let cur2 = cur2Select.value
        let exchangerate = Number(rates[cur2]) / Number(rates[cur1])
        infoBox.innerText = `1 ${cur1} = ${exchangerate} ${cur2}`
        if (cur1Field.value != "") {
            cur2Field.value = (cur1Field.value * exchangerate).toFixed(2)
        }
        else {
            cur2Field.value = ""
        }
    }
    calculate()

}

get()

