const express = require("express")
const app = express()
let PORT = 8080

app.use(express.urlencoded({ extended: true }))

app.get('/form', (req, res) => {
    res.sendFile(`${__dirname}/index.html`)
})

app.post('/form/submit', (req, res) => {
    let data = req.body
    res.send(`
    <table class="table">
        <tr>
            <td>Your Name : </td>
            <td>${data.name}</td>
        </tr>

        <tr>
            <td>Your Email : </td>
            <td>${data.email}</td>
        </tr>

        <tr>
            <td>Your Message : </td>
            <td>${data.message}</td>
        </tr>

        <tr>
            <td>Your Choice : </td>
            <td>${data.choice}</td>
        </tr>
    </table>
    `)
})

app.listen(PORT, () => {
    console.log("Server Started")
})
