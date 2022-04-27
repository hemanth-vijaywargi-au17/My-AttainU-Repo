// Dependencies
const express = require('express')
const mongoose = require('mongoose')
const fileUpload = require('express-fileupload')  // MiddleWare to handle incoming Files
const expSession = require('express-session')  // MiddleWare to handle Authentication

// Server
const app = express();
const port = process.env.PORT || 4000
app.use(express.static('public'))

// MiddleWares
app.use(express.urlencoded({ extended: true }))  // MiddleWare for handling Textual Data
app.use(fileUpload())  //MiddleWare for handling File Data
const oneDay = 1000 * 60 * 60 * 24;
app.use(expSession({
    secret: "srghsehbtbhdtbhdtbhaergqwhjklekjrhe",
    saveUninitialized: true,
    resave: false,
    cookie: { maxAge: oneDay }
}))

// Database
const dbHelper = require('./db.js')
dbHelper.dbInit()

// Schema
const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    imageUrl: {
        type: String,
    }
})

// Model
const UserModel = mongoose.model('user', UserSchema)

// Add User
app.post("/signup", async (req, res) => {
    try {
        // Textual Data
        const data = req.body

        if (req.files) {
            // File Data (any type of file)
            const fileData = req.files.userImage // userImage is the "name" of our file input field.

            // Making a unique Filename using md5 and actual name of the file when uploaded.
            const fileName = `${fileData.md5}-${fileData.name}`

            // Path where the file is to be stored on the server.
            const filePath = `${__dirname}/public/userImages/${fileName}`

            // Saving the path/url of our file in text data
            data.imageUrl = `/userImages/${fileName}`

            // Moving the uploded file to the specified filePath
            fileData.mv(filePath)
        }
        else {
            data.imageUrl = `/userImages/default.png`
        }

        // Inserting the Textual data in our mongodb Model
        const insertedData = await UserModel.create(data)

        // Sending Textual data as a response to successful submission of data
        res.status(201).send(insertedData)
    }
    catch (err) {
        res.send({
            error: true,
            errorObj: err
        })
    }
})

app.post('/login', (req, res) => {
    const data = req.body
    UserModel.exists({ email: data.email }, (error, result) => {
        if (error) {
            res.send(error)
        } else {
            if (result) {
                req.session.user = data.email
                req.session.loggedIn = true
                res.redirect(`/profile`)
            }
            else {
                res.send("User Doesn't Exist")
            }
        }
    })
})

function checkAuth(req, res, next) {
    if (req.session.user && req.session.loggedIn == true) {
        next()
    } else {
        res.redirect('/login')
    }
}

app.get('/profile', checkAuth, (req, res) => {
    res.sendFile(`${__dirname}/views/profile`)
})

app.use(express.static('views'))

// Starting the Server
app.listen(port, () => {
    console.log(`app listening on port : ${port}`);
});