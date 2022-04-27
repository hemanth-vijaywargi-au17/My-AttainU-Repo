// Dependencies
const express = require("express");
const fileUpload = require("express-fileupload");
require('dotenv').config()

// Server
const app = express();
const PORT = process.env.PORT;

// MiddleWares
app.use(express.urlencoded({ extended: true }));
app.use(fileUpload());
app.use(express.json())
app.use(express.static("public"));

// Database
require("./db.js").dbConnect();

// Routes
const { UserRoutes } = require("./routes/UserRoutes.js");
app.use("/api", UserRoutes);

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
