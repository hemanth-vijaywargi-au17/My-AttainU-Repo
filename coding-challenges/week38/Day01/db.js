const mongoose = require("mongoose");

// Database
async function dbConnect() {
  await mongoose.connect(process.env.DB_URL);
}

module.exports = { dbConnect };
