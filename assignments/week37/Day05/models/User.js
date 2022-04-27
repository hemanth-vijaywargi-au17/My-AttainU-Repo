const { Schema, model } = require("mongoose");

// Schema
const UserSchema = new Schema({
  name: {
    type: String,
    required: true,
  },
  imageURL: {
    type: String,
  },
});

// Model
const UserModel = model("user", UserSchema);

module.exports = UserModel;
