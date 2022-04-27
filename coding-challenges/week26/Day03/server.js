const express = require('express')
const { MongoClient } = require('mongodb')

const app = express()
app.use(express.urlencoded({ extended: true }))
let PORT = 4000

// MongoDB
let userName = 'DBAdmin'
let password = 'lhmGNLpqObqGLp66'
let dbName = 'product_database'
let url = `mongodb+srv://${userName}:${password}@cluster0.p2fbb.mongodb.net/${dbName}?retryWrites=true&w=majority`
const client = new MongoClient(url)

app.get('/product', (req, res) => {
    res.sendFile(`${__dirname}/product_form.html`)
})

app.get('/user', (req, res) => {
    res.sendFile(`${__dirname}/user_form.html`)
})

app.post('/product', async (req, res) => {
    await client.connect()
    const db = client.db(dbName)
    const product_collection = db.collection("product_collection")
    await product_collection.insertOne(req.body)
    res.send("Product Entry Saved!")
})

app.post('/user', async (req, res) => {
    await client.connect()
    const db = client.db(dbName)
    const user_collection = db.collection("user_collection")
    await user_collection.insertOne(req.body)
    res.send("User Saved!")
})

app.get('/', async (req, res) => {
    await client.connect()
    const db = client.db(dbName)
    const product_collection = db.collection("product_collection")
    const user_collection = db.collection("user_collection")
    const products = await product_collection.find({}).toArray()
    const users = await user_collection.find({}).toArray()
    res.send({ Products: products, Users: users })
})

app.listen(PORT, () => {
    console.log("Server Started !")
})