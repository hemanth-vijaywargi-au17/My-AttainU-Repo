// Dependencies
const express = require("express");
const fileUpload = require("express-fileupload");
require("dotenv").config();

// Creating Server
const app = express();
const PORT = process.env.PORT;

// Database
require("./db.js").dbConnect();

// MiddleWares
app.use(fileUpload());
app.use(express.urlencoded({ extended: true }));

// Using ejs template engine
app.set("view engine", "ejs");

// Routes
const routes = require("./routes/routes");
app.use(routes);

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
