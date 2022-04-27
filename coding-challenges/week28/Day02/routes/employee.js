// Depndencies
const EmployeeModel = require('../models/Employee.js')
const { Router } = require('express')
const jwt = require('jsonwebtoken')

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
        const requestedData = await EmployeeModel.findById(id)
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