const express = require('express')

const app = express()
app.use(express.urlencoded({ extended: true }))
let port = process.env.PORT || 4000

app.use(express.static('projects'))

app.listen(port, () => {
    console.log(`Server Started at PORT : ${port}`)
})
