var rockBtn = document.getElementById("rock")
var paperBtn = document.getElementById("paper")
var scissorsBtn = document.getElementById("scissors")

var message1 = document.getElementById("message1")
var message2 = document.getElementById("message2")

rockBtn.addEventListener("click",game)
paperBtn.addEventListener("click",game)
scissorsBtn.addEventListener("click",game)

function game(e){
    var moves = ["rock","paper","scissors"]
    var humanMove = e.currentTarget.id
    var computerMove = moves[Math.floor(Math.random() * 3)]
    message1.innerText = `You : ${humanMove} \n Computer : ${computerMove}`
    var winMessage;
    if (humanMove == computerMove){
        winMessage = "Its a Tie!"
    }
    else if(humanMove == "rock" && computerMove == "paper"){
        winMessage = "Computer Wins!"
    }
    else if(humanMove == "rock" && computerMove == "scissors"){
        winMessage = "You Win!"
    }
    else if(humanMove == "paper" && computerMove == "rock"){
        winMessage = "You Win!"
    }
    else if(humanMove == "paper" && computerMove == "scissors"){
        winMessage = "Computer Wins!"
    }
    else if(humanMove == "scissors" && computerMove == "rock"){
        winMessage = "Computer Wins!"
    }
    else if(humanMove == "scissors" && computerMove == "paper"){
        winMessage = "You Win!"
    }
    message2.innerText = winMessage
}