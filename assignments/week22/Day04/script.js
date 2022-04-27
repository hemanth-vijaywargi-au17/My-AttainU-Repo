var playBtn = document.getElementById("play")
playBtn.addEventListener("click", game)

function game() {
    playBtn.style.display = "none"
    var messageBox = document.getElementById("message")
    var boxes = document.getElementsByClassName("box")
    var gameBox = document.getElementById("gameBox")
    var matrix = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]]
    var players = {
        "x": { color: "indianred" },
        "o": { color: "sandybrown" }
    }
    var currentPlayer = "x"
    messageBox.innerText = currentPlayer + " Turn"

    var enter = function (e) {
        e.currentTarget.innerText = currentPlayer
        e.currentTarget.style.color = players[currentPlayer].color
        e.currentTarget.style.filter = "brightness(60%)"
    }
    var out = function (e) {
        e.currentTarget.innerText = ""
        e.currentTarget.style.filter = "brightness(100%)"
    }
    var click = function (e) {
        e.currentTarget.innerText = currentPlayer
        e.currentTarget.style.color = players[currentPlayer].color
        e.currentTarget.style.filter = "brightness(100%)"
        e.currentTarget.removeEventListener("mouseenter", enter)
        e.currentTarget.removeEventListener("mouseout", out)
        e.currentTarget.removeEventListener("click", click)

        parentID = e.currentTarget.parentElement.id;
        row = Number(parentID[parentID.length - 1]) - 1;
        boxClass = e.currentTarget.classList[1]
        col = Number(boxClass[boxClass.length - 1]) - 1
        recordMove(row, col, currentPlayer)

        if (checkWin() == true) {
            messageBox.innerText = currentPlayer + " wins"
            for (i = 0; i < boxes.length; i++) {
                boxes[i].removeEventListener("mouseenter", enter)
                boxes[i].removeEventListener("mouseout", out)
                boxes[i].removeEventListener("click", click)
            }
            playBtn.style.display = "initial"
            playBtn.innerText = "Play Again"
            gameBox.style.filter = "brightness(60%)"
            return
        }

        if (checkTie() == true) {
            messageBox.innerText = "Match Tied"
            playBtn.style.display = "initial"
            playBtn.innerText = "Play Again"
            return
        }

        if (currentPlayer == "x") {
            currentPlayer = "o"
        }
        else {
            currentPlayer = "x"
        }
        messageBox.innerText = currentPlayer + " Turn"
    }
    function reset() {
        for (let i = 0; i < boxes.length; i++) {
            boxes[i].addEventListener("mouseenter", enter)
            boxes[i].addEventListener("mouseout", out)
            boxes[i].addEventListener("click", click)
            boxes[i].style.backgroundColor = "white"
            boxes[i].innerText = ""
        }
        gameBox.style.filter = "brightness(100%)"
    }
    reset()
    function recordMove(row, col, player) {
        matrix[row][col] = player
    }

    function checkWin() {
        // check for horizontal win
        for (i = 0; i < 3; i++) {
            if ((matrix[i][0] == matrix[i][1]) && (matrix[i][1] == matrix[i][2])) {
                return true
            }
        }

        // check for vertical win
        for (i = 0; i < 3; i++) {
            if ((matrix[0][i] == matrix[1][i]) && (matrix[1][i] == matrix[2][i])) {
                return true
            }
        }

        //check for diagonal win
        var diagonal = (matrix[0][0] == matrix[1][1]) && (matrix[1][1] == matrix[2][2])
        var antiDiagonal = (matrix[0][2] == matrix[1][1]) && (matrix[1][1] == matrix[2][0])
        if ((diagonal) || (antiDiagonal)) {
            return true
        }

        return false
    }

    function checkTie() {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (matrix[i][j] != "x") {
                    if (matrix[i][j] != "o") {
                        return false
                    }
                }
            }
        }
        return true
    }

}
