const { Schema, model } = require("mongoose");

const studentSchema = Schema({
  name: {
    type: Schema.Types.String,
    required: true,
  },
  id: {
    type: Schema.Types.Number,
    required: true,
  },
  course: {
    type: Schema.Types.String,
  },
});

const studentModel = model("student", studentSchema);

module.exports = { studentModel };
