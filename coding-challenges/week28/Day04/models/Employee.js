const mongoose = require('mongoose')

// Schema
const EmployeeSchema = new mongoose.Schema({
    emp_name: {
        type: String,
        required: true
    },
    designation: {
        type: String,
        required: true
    },
    salary: {
        type: Number,
        required: true
    },
    hireDate: {
        type: Date,
        required: true
    },
    active: {
        type: Boolean,
        required: true
    }
})

// Model
const EmployeeModel = mongoose.model('employee', EmployeeSchema)

module.exports = EmployeeModel