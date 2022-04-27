const express = require('express');

const app = express()
let port = process.env.PORT || 4000

app.use(logger)
function logger(req,res,next){
    log = `${new Date()} ${req.method} ${req.path} ${req.ip}`
    console.log(log)
    next()
}

app.get('/api', (req, res) => {
   res.send("You have Done a GET Request")
})

app.post('/api', (req, res) => {
    res.send("You have Done a POST Request")
})

app.put('/api', (req, res) => {
    res.send("You have Done a PUT Request")
})

app.delete('/api', (req, res) => {
    res.send("You have Done a DELETE Request")
})

app.listen(port, () => {
    console.log(`Server Started at PORT : ${port}.`)
})
