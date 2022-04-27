const express = require('express')
const { MongoClient } = require('mongodb')

const app = express()
app.use(express.urlencoded({ extended: true }))
let PORT = 4000

// MongoDB
let userName = 'DBAdmin'
let password = 'lhmGNLpqObqGLp66'
let dbName = 'survey_database'
let collectionName = 'survey_collection'
let url = `mongodb+srv://${userName}:${password}@cluster0.p2fbb.mongodb.net/${dbName}?retryWrites=true&w=majority`
const client = new MongoClient(url)


app.get('/favoriteSurvey', (req, res) => {
    res.sendFile(`${__dirname}/form.html`)
})

app.post('/favoriteSurvey', async (req, res) => {
    await client.connect()
    const db = client.db(dbName)
    const collection = db.collection(collectionName)
    await collection.insertOne(req.body)
    res.send("Entry Saved!")
})

app.get('/favoriteSurveyResults', async (req, res) => {
    await client.connect()
    const db = client.db(dbName)
    const collection = db.collection(collectionName)
    const response = await collection.find({}).toArray()
    res.send(response)
})

app.listen(PORT, () => {
    console.log("Server Started !")
})