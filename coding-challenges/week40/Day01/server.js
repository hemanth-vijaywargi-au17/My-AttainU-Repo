// Dependencies
const express = require("express");
const graphqlMiddleWare = require("./graphqlMiddleware");
require("dotenv").config();

// Creating the express server
const app = express();
const PORT = process.env.PORT || 5000;

// Using Graphql middleware
app.use("/graphql", graphqlMiddleWare);

// Connecting to DataBase
require("./db").dbConnect();

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
