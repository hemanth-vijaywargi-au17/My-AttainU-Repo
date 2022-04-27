// Dependencies
const express = require("express");
const { dbConnect } = require("./db.js");
require("dotenv").config();

// Creating Server
const app = express();
const PORT = process.env.PORT;

// Database
dbConnect();
const { MovieModel } = require("./models/Movie.js");

// Dummy Route
app.get("/", async (req, res) => {
  let pipeline1 = [
    {
      $match: {
        rated: "NOT RATED",
        year: 2000,
      },
    },
  ];
  let response1 = await MovieModel.aggregate(pipeline1);

  let expression1 = { genres: "Comedy", year: 2016 };
  let expression2 = { "imdb.rating": 7 };
  let pipeline2 = [
    { $match: { $or: [expression1, expression2] } },
    { $limit: 11 },
  ];
  let response2 = await MovieModel.aggregate(pipeline2);

  res.send({ response1: response1, response2: response2 });
});

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
