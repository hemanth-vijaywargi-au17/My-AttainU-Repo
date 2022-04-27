const { connect } = require("mongoose");

async function dbConnect() {
  const connection = await connect(process.env.DB_URL);
  return connection;
}

module.exports = { dbConnect };
