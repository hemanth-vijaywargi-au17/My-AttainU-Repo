var solve_btn = document.getElementById("solve")
solve_btn.addEventListener("click",function(){
    var inputNumber1 = document.getElementById("number1")
    var inputNumber2 = document.getElementById("number2")
    var answer_box = document.getElementById("answer")

    var number1 = Number(inputNumber1.value)
    var number2 = Number(inputNumber2.value)
    var sum = number1 + number2

    answer_box.innerHTML = sum

})
