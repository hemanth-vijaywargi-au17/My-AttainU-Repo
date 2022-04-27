const mongoose = require("mongoose");

// Database
async function dbConnect() {
  let result = await mongoose.connect(process.env.DB_URL);
  return result.connection.db
}

module.exports = { dbConnect };
