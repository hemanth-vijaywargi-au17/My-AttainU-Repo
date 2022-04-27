let addBtn = document.getElementById("addBtn")
let addBox = document.getElementById("addBox")
let cutBtn = document.getElementById("cutBtn")
let questionField = document.getElementById("question")
let answerField = document.getElementById("answer")
let saveBtn = document.getElementById("saveBtn")
let flashBox = document.getElementById("flashBox")

addBtn.addEventListener("click", e => {
    addBox.style.display = "block"
})

cutBtn.addEventListener("click", e => {
    addBox.style.display = "none"
})

saveBtn.addEventListener("click", e => {
    // Building our FlashCard
    let parent = document.createElement("div")
    parent.setAttribute("class", "flashcard d-flex flex-column p-4 justify-content-between")

    let qBox = document.createElement("div")
    qBox.setAttribute("class", "question mb-2")
    qBox.innerText = questionField.value
    parent.appendChild(qBox)

    let sBox = document.createElement("div")
    sBox.setAttribute("class", "show mb-3")
    sBox.innerText = "Show/Hide Answer"
    parent.appendChild(sBox)

    let aBox = document.createElement("div")
    aBox.setAttribute("class", "answer mb-3")
    aBox.innerText = answerField.value
    aBox.style.display = "none"
    parent.appendChild(aBox)

    let btnBox = document.createElement("div")
    btnBox.setAttribute("class", "d-flex justify-content-between")
    parent.appendChild(btnBox)

    let eBtn = document.createElement("button")
    eBtn.setAttribute("class", "editBtn")
    eBtn.innerText = "EDIT"
    btnBox.appendChild(eBtn)

    let dBtn = document.createElement("button")
    dBtn.setAttribute("class", "deleteBtn")
    dBtn.innerText = "DELETE"
    btnBox.appendChild(dBtn)

    // Adding Event Listeners to Various Elements of our Flashcard
    sBox.addEventListener("click", e => {
        if (aBox.style.display == "none") {
            aBox.style.display = "block"
        }
        else {
            aBox.style.display = "none"
        }
    })

    eBtn.addEventListener("click", e => {
        questionField.value = qBox.innerText
        answerField.value = aBox.innerText
        parent.remove()
        addBox.style.display = "block"
    })

    dBtn.addEventListener("click", e => {
        parent.style.animation ="flashcard_disappear 0.3s ease-in"
        setTimeout(function () { parent.remove() }, 300);

    })

    // Finally Appending our FlashCard to FlashBox
    flashBox.appendChild(parent)

    // Clearing Input Fields
    questionField.value = ""
    answerField.value = ""
})


