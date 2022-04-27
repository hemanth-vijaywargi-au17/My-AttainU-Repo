let symbols = ["!", "#", "$", "%", "&", "*",
    "<", ">", "?", "@", "^", "_"]

let numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

let upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']

let lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']

function generate2(length = 10, u = true, l = true, s = true, n = true) {
    let password = ""
    let chars = []
    if (u) {
        chars.push(upper)
    }
    if (l) {
        chars.push(lower)
    }
    if (s) {
        chars.push(symbols)
    }
    if (n) {
        chars.push(numbers)
    }
    for (let i = 0; i < length; i++) {
        let arr = chars[Math.floor(Math.random() * chars.length)]
        let char = arr[Math.floor(Math.random() * arr.length)]
        password += char
    }
    return password
}

function generate1(length = 10) {
    let password = ""
    for (let i = 0; i < length; i++) {
        let code = Math.floor(Math.random() * 94) + 33
        password += String.fromCharCode(code)
    }
    return password
}

console.log(generate1(14))
console.log(generate2(14, true, true, true, true))