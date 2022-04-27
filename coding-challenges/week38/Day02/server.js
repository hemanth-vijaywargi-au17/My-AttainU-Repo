// Lawrence Bhai copy kar rahe ho toh credit dena mat bhulna (-_-) (-_-) (-_-) i am Watching
// - Hemanth

// Dependencies
const express = require("express");
const { MongoClient } = require("mongodb");
require("dotenv").config();

// Creating the Server
const app = express();
const PORT = process.env.PORT;

// Connecting to Database-Client
const client = new MongoClient(process.env.DB_URL);
async function dbConnect() {
  await client.connect();
}
dbConnect();

// Database and Collection (which we want to use)
const database = client.db("sample_airbnb");
const collection = database.collection("listingsAndReviews");

// Dummy Route to show result
app.get("/", async (req, res) => {
  /* 
  CC Requirement
  Find all the listings where, the country is Spain and price is less than equal to 15 and review_scores_rating in 
  review_scores is greater than and equal to 75. The result should be ordered in descending order based on the price.
  */

  // Creating pipeline according to the requirement
  let pipeline = [
    {
      $match: {
        "address.country": "Spain",
        price: { $lte: 15 },
        "review_scores.review_scores_rating": { $gte: 75 },
      },
    },
    {
      $sort: {
        price: -1,
      },
    },
  ];

  // aggregate() returns a Cursor which needs to be converted to an Array.
  const response = await collection.aggregate(pipeline).toArray();

  res.send(response);
});

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at ${PORT}`);
});
