let tbody = document.getElementById("tbody")
let input = document.getElementById("input")
let promiseObj = fetch("https://jsonplaceholder.typicode.com/users")

let capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}


promiseObj.then(obj => obj.json()).then(array => {
    for (let i = 0; i < array.length; i++) {
        let curName = array[i].name.split(" ")
        let firstname, lastname
        if (curName[0].toLowerCase() == "mr." || curName[0].toLowerCase() == "mrs.") {
            firstname = curName[0] + " " + curName[1]
            lastname = curName[2]
        }
        else if (curName.length == 3) {
            firstname = curName[0]
            lastname = curName[1] + " " + curName[2]
        }
        else {
            firstname = curName[0]
            lastname = curName[1]
        }

        let id = array[i].id
        let row = document.createElement("tr")
        row.setAttribute("id", id)
        let td1 = document.createElement("td")
        let td2 = document.createElement("td")
        row.appendChild(td1)
        row.appendChild(td2)
        td1.innerText = firstname
        td2.innerText = lastname
        tbody.appendChild(row)
    }
    let og = tbody.innerHTML

    input.addEventListener("input", e => {
        searchTerm = e.currentTarget.value.toLowerCase()
        for (let i = 0; i < array.length; i++) {

            let curElement = document.getElementById(`${array[i].id}`)
            let td1 = curElement.firstChild
            let td2 = curElement.lastChild

            let curName = array[i].name.toLowerCase()
            let curName1 = array[i].name.split(" ")
            let first, last

            if (curName1[0].toLowerCase() == "mr." || curName1[0].toLowerCase() == "mrs.") {
                first = curName1[0] + " " + curName1[1]
                last = curName1[2]
            }
            else if (curName1.length == 3) {
                first = curName1[0]
                last = curName1[1] + " " + curName1[2]
            }
            else {
                first = curName1[0]
                last = curName1[1]
            }
            first = first.toLowerCase()
            last = last.toLowerCase()

            if (searchTerm != "") {
                if (curName.includes(searchTerm)) {
                    curElement.style.display = "table-row"

                    // Highlighting searchTerm
                    if (first.includes(searchTerm)) {
                        let res = ""
                        let splitted = first.split(searchTerm)
                        let cap = true
                        for (let i = 0; i < splitted.length - 1; i++) {
                            if (splitted[i] == "" && i == 0) {
                                res += (splitted[i] + "<span class='highlight'>" + capitalize(searchTerm) + "</span>")
                                cap = false
                            }
                            else {
                                res += (splitted[i] + "<span class='highlight'>" + searchTerm + "</span>")
                            }
                        }
                        if (cap) {
                            res = capitalize(res)
                        }
                        res += splitted[splitted.length - 1]
                        td1.innerHTML = res
                    }
                    else {
                        td1.innerHTML = ""
                        td1.innerText = capitalize(first)
                    }

                    if (last.includes(searchTerm)) {
                        let res = ""
                        let splitted = last.split(searchTerm)
                        let cap = true
                        for (let i = 0; i < splitted.length - 1; i++) {
                            if (splitted[i] == "" && i == 0) {
                                res += (splitted[i] + "<span class='highlight'>" + capitalize(searchTerm) + "</span>")
                                cap = false
                            }
                            else {
                                res += (splitted[i] + "<span class='highlight'>" + searchTerm + "</span>")
                            }
                        }
                        if (cap) {
                            res = capitalize(res)
                        }
                        res += splitted[splitted.length - 1]
                        td2.innerHTML = res
                    }
                    else {
                        td2.innerHTML = ""
                        td2.innerText = capitalize(last)
                    }

                }
                else {
                    curElement.style.display = "none"
                }
            }
            else {
                tbody.innerHTML = og
            }

        }
    })

})

promiseObj.catch(response => console.log(response))




