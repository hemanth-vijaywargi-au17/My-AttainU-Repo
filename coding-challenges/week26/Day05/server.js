// Book REST API
// Deployed at https://mybook-rest-api.herokuapp.com (No HTML , can Test with Insomnia)
// Nothing at root Route '/' , see below to use various Routes.

const express = require('express')
const { MongoClient, ObjectId } = require('mongodb')

const app = express()
app.use(express.urlencoded({ extended: true }))
let port = process.env.PORT || 4000

// MongoDB
let userName = 'DBAdmin'
let password = 'lhmGNLpqObqGLp66'
let dbName = 'book_database'
let url = `mongodb+srv://${userName}:${password}@cluster0.p2fbb.mongodb.net/${dbName}?retryWrites=true&w=majority`
const client = new MongoClient(url)

async function init() {
    await client.connect()
}
init()
let db = client.db(dbName)
let book_collection = db.collection('book_collection')

// Get all Books
app.get('/books', async (req, res) => {
    let response = await book_collection.find({}).toArray()
    res.send(response)
})

// Get Single Book
app.get('/books/:uniqueId', async (req, res) => {
    let idObj = new ObjectId(req.params.uniqueId)
    let response = await book_collection.findOne({ "_id": idObj })
    res.send(response)
})

// Add Book
app.post('/books', async (req, res) => {
    let insertedResult = await book_collection.insertOne(req.body)
    res.send(insertedResult)
})

// Update Book
app.put('/books/:uniqueId', async (req, res) => {
    let idObj = new ObjectId(req.params.uniqueId)
    let newData = req.body
    let updatedResult = await book_collection.updateOne({ "_id": idObj }, { $set: newData })
    res.send(updatedResult)
})

// Delete Book
app.delete('/books/:uniqueId', async (req, res) => {
    let idObj = new ObjectId(req.params.uniqueId)
    let deletedResult = await book_collection.deleteOne({ "_id": idObj })
    res.send(deletedResult)
})

app.listen(port, () => {
    console.log(`Server Started at PORT : ${port}.`)
})
