// My First REST API :)
const express = require('express')
const { MongoClient, ObjectId } = require('mongodb')

const app = express()
app.use(express.urlencoded({ extended: true }))
let PORT = 4000

// MongoDB
let userName = 'DBAdmin'
let password = 'lhmGNLpqObqGLp66'
let dbName = 'hotel_database'
let url = `mongodb+srv://${userName}:${password}@cluster0.p2fbb.mongodb.net/${dbName}?retryWrites=true&w=majority`
const client = new MongoClient(url)

// Get all Hotels
app.get('/hotels', async (req, res) => {
    await client.connect()
    let db = client.db(dbName)
    let hotel_collection = db.collection('hotel_collection')
    let response = await hotel_collection.find({}).toArray()
    res.send(response)
})

// Get Single Hotel
app.get('/hotels/:uniqueId', async (req, res) => {
    await client.connect()
    let db = client.db(dbName)
    let hotel_collection = db.collection('hotel_collection')
    let idObj = new ObjectId(req.params.uniqueId)
    let response = await hotel_collection.findOne({ "_id": idObj })
    res.send(response)
})

// Add Hotel
app.post('/hotels', async (req, res) => {
    await client.connect()
    let db = client.db(dbName)
    let hotel_collection = db.collection('hotel_collection')
    let insertedResult = await hotel_collection.insertOne(req.body)
    res.send(insertedResult)
})

// Update Hotel
app.put('/hotels/:uniqueId', async (req, res) => {
    await client.connect()
    let db = client.db(dbName)
    let hotel_collection = db.collection('hotel_collection')
    let idObj = new ObjectId(req.params.uniqueId)
    let newData = req.body
    let updatedResult = await hotel_collection.updateOne({ "_id": idObj }, { $set: newData })
    res.send(updatedResult)
})

// Delete Hotel
app.delete('/hotels/:uniqueId', async (req, res) => {
    await client.connect()
    let db = client.db(dbName)
    let hotel_collection = db.collection('hotel_collection')
    let idObj = new ObjectId(req.params.uniqueId)
    let deletedResult = await hotel_collection.deleteOne({ "_id": idObj })
    res.send(deletedResult)
})

app.listen(PORT, () => {
    console.log("Server Started !")
})