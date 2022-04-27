// Depndencies
const EmployeeModel = require('../models/Employee.js')
const { Router } = require('express')
const jwt = require('jsonwebtoken')
const redis = require('redis')

// Redis
const REDIS_PORT = process.env.REDIS_PORT || 6379
const redisClient = redis.createClient({port: REDIS_PORT})

const {promisify} = require('util')
const getRedisAsync = promisify(redisClient.get).bind(redisClient)

// Router
const employeeRoutes = Router()

// Authentication MiddleWare
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

employeeRoutes.use(checkJWTToken)


// Routes :
// Add Employee
employeeRoutes.post('/', async (req, res) => {
    try {
        const data = req.body
        const insertedData = await EmployeeModel.create(data)
        res.status(201).json(insertedData)

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
        })
    }
})

// Get single Employee Details
employeeRoutes.get('/:uniqueId', async (req, res) => {
    try {
        const id = req.params.uniqueId
        const data = await getRedisAsync(id)

        if (data) {
            const employeeObj = JSON.parse(data)
            return res.json(employeeObj)
        }

        const requestedData  = await EmployeeModel.findById(id)
        
        redisClient.setex(id, 36000,  JSON.stringify(requestedData) )
    
        res.json(requestedData)

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
        })
    }
})

// Get all Employee Details
employeeRoutes.get('/', async (req, res) => {
    try {
        const requestedData = await EmployeeModel.find({})
        res.json(requestedData)

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
        })
    }
})

// Update Employee
employeeRoutes.put('/:uniqueId', async (req, res) => {
    try {
        const id = req.params.uniqueId
        const data = req.body
        const updatedData = await EmployeeModel.findByIdAndUpdate(id, data, { new: true })
        res.json(updatedData)

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
        })
    }
})

// Delete Employee
employeeRoutes.delete('/:uniqueId', async (req, res) => {
    try {
        const id = req.params.uniqueId
        const deletedData = await EmployeeModel.findByIdAndDelete(id)
        res.json(deletedData)

    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
        })
    }
})

module.exports = employeeRoutes