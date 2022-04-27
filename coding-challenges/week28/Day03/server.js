// Employee REST API

// Dependencies
const express = require('express')
const morgan = require('morgan')
const jwt = require('jsonwebtoken')

// Server
const app = express();
const port = process.env.PORT || 4000

// MiddleWares
app.use(express.urlencoded({ extended: true }))
app.use(express.json()) // Json MiddleWare
app.use(morgan('dev'))  // Logger MiddleWare

// Database
const dbHelper = require('./db.js');
dbHelper.dbInit()

// Employee Routes
const employeeRoutes = require('./routes/employee.js');
app.use('/employees', employeeRoutes)

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

        if (data.email == "hemanthvj12@gmail.com" && data.password == "Password") {
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


// Starting the Server
app.listen(port, () => {
    console.log(`app listening on port : ${port}`);
});

