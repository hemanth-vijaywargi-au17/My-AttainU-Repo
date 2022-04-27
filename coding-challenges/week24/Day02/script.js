let getBtn = document.getElementById("getBtn")
let img = document.getElementById("img")
getBtn.addEventListener("click", handler)

function handler(e) {
    promiseObj = fetch("https://dog.ceo/api/breeds/image/random")
    promiseObj.then((obj) => obj.json()).then(fulfilled)
    promiseObj.catch(rejected)
}

function fulfilled(response) {
    img.setAttribute("src", response.message)
    img.style.width = "fit-content"
}

function rejected() {
    img.setAttribute("alt", "Unable to get an Image :( , try Again")
    img.setAttribute("src", "")
    img.style.width = "300px"
}

handler()
