let inputField = document.getElementById("input")
let submitBtn = document.getElementById("submit")
let messageBox = document.getElementById("message")

submitBtn.addEventListener("click", e => {
    let input = inputField.value.split(",")
    let str1 = input[0]
    let str2 = input[1]
    if (str1.length != str2.length) {
        messageBox.innerText = 'Unequal Length Strings!'
    } else {
        messageBox.innerText = hammingDist(str1, str2)
    }
})

function hammingDist(s1, s2) {
    p1 = 0
    p2 = 0
    res = 0
    while (p1 < s1.length && p2 < s2.length) {
        if (s1[p1] != s2[p2]) {
            res += 1
        }
        p1 += 1
        p2 += 1
    }
    return res
}
