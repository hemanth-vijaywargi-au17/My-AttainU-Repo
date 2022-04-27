// Dependencies
const express = require('express')
const mongoose = require('mongoose')
const jwt = require('jsonwebtoken')

// Server
const app = express();
const port = process.env.PORT || 4000

// MiddleWares
app.use(express.urlencoded({ extended: true }))

// Database
const dbHelper = require('./db.js');
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
    }
})

// Model
const UserModel = mongoose.model('user', UserSchema)

function checkJWTToken(req, res, next) {

    try {
        const authTokenDecodedData = jwt.verify(req.header('token'), "This is my secret key")
        next()
    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
            message: "Invalid Token",
        })
    }
}

app.post('/login', async (req, res) => {

    try {
        const data = req.body

        //validations
        if (!data.email || !data.password) {
            res.json({
                error: true,
                message: "Empty data"
            })
            return
        }

        let response = await UserModel.find({ email: data.email })
        if (response.length == 0) {
            res.json({
                error: true,
                message: "User Does Not Exist!"
            })
            return
        }

        if (data.password == response[0].password) {
            //generate a token
            const secret = "This is my secret key"
            const jwtToken = jwt.sign({ currentUser: data.email }, secret, { expiresIn: '2d' })

            res.json({
                error: false,
                message: "User Logged in",
                token: jwtToken
            })
            return
        }

        res.json({
            error: true,
            message: "User credentials does not match"
        })

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
            message: "Unknown Error"
        })
    }

})

app.get('/profile', checkJWTToken, async (req, res) => {
    res.send("Welcome to the Profile")
})

// Add User
app.post("/signup", async (req, res) => {
    try {
        const data = req.body
        let response = await UserModel.find({email:data.email})
        if(response.length!=0){
            res.json({
                error: true,
                message: "User Already Exists",
            })
            return
        }
        // Inserting the data in our mongodb Model
        const insertedData = await UserModel.create(data)

        // Sending data as a response to successful submission of data
        res.status(201).send({ message: "Sign Up Successful", details: insertedData })
    }
    catch (err) {
        res.send({
            error: true,
            errorObj: err
        })
    }
})

// Starting the Server
app.listen(port, () => {
    console.log(`app listening on port : ${port}`);
});

