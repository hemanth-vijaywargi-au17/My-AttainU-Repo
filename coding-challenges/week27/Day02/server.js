const express = require('express');
const mongoose = require('mongoose')
const app = express();
const port = process.env.PORT || 4000
const dbHelper = require('./db.js')
dbHelper.dbInit()
app.use(express.urlencoded({ extended: true }))

const InterviewSchema = new mongoose.Schema({
    title: {
        type: String
    },
    firstName: {
        type: String,
        required: true
    },
    lastName: {
        type: String,
        required: true
    },
    interviewDate: {
        type: String
    },
    interviewTime: {
        type: String
    },
    candidatePosition: {
        type: String
    },
    department: {
        type: String
    },
    hiringManager: {
        type: String
    }
})

const InterviewModel = mongoose.model('interview_info', InterviewSchema)

app.use(express.static('public'))

// Add InterviewInfo
app.post("/interview_infos", async (req, res) => {
    try {
        const data = req.body
        const insertedData = await InterviewModel.create(data)
        res.send(insertedData)
    }
    catch (err) {
        res.send({
            error: true,
            errorObj: err
        })
    }
})

// Update InterviewInfo
app.post("/interview_infos/:uniqueID", async (req, res) => {
    try {
        const data = req.body
        const updatedData = await InterviewModel.findByIdAndUpdate(req.params.uniqueID, data)
        res.send(updatedData)
    }
    catch (err) {
        res.send({
            error: true,
            errorObj: err
        })
    }
})

app.listen(port, () => {
    console.log(`app listening on port : ${port}`);
});