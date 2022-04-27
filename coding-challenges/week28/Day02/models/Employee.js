const mongoose = require('mongoose')

// Schema
const EmployeeSchema = new mongoose.Schema({
    emp_name: {
        type: String,
        required: true
    },
    job_name: {
        type: String,
        required: true
    },
    hire_date: {
        type: Date,
        required: true
    },
    salary: {
        type: Number,
        required: true
    },
})

// Model
const EmployeeModel = mongoose.model('employee', EmployeeSchema)

module.exports = EmployeeModel