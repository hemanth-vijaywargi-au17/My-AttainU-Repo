const { Schema, model } = require("mongoose");

// Schema
const UserSchema = new Schema({
  id: {
    type: Number,
    required: true,
  },
  username: {
    type: String,
    required: true,
  },
  age: {
    type: Number,
  },
});

// Model
const UserModel = model("user", UserSchema);

module.exports = UserModel;
