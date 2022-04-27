// Dependencies
const express = require("express");
require("dotenv").config();

// Creating Server
const app = express();
const PORT = process.env.PORT;

// Database
require("./db.js").dbConnect();

// MiddleWares
app.use(express.json());

// Routes
const routes = require("./routes/routes");
app.use(routes);

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
