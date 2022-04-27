// Queue Emulator
// Deployed at https://queue-emulator.herokuapp.com
// Check it out!

const express = require('express')

const app = express()
app.use(express.urlencoded({ extended: true }))
let port = process.env.PORT || 4000

app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/index.html`)
})

app.get('/styles.css', (req, res) => {
    res.sendFile(`${__dirname}/styles.css`)
})

app.get('/script.js', (req, res) => {
    res.sendFile(`${__dirname}/script.js`)
})

app.listen(port, () => {
    console.log(`Server Started at PORT : ${port}`)
})
