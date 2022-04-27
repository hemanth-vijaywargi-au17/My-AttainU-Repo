const { Schema, model } = require("mongoose");

// Schema
const CarSchema = new Schema({
  model: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  customer_id: { type: Schema.Types.ObjectId, ref: "customer" },
});

// Model
const CarModel = model("car", CarSchema);

module.exports = CarModel;
