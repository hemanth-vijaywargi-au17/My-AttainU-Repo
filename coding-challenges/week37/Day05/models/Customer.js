const { Schema, model } = require("mongoose");

// Schema
const CustomerSchema = new Schema({
  name: {
    type: String,
    required: true,
  },
  cars: {
    type: [{ type: Schema.Types.ObjectId, ref: "car" }],
  },
});

// Model
const CustomerModel = model("customer", CustomerSchema);

module.exports = CustomerModel;
