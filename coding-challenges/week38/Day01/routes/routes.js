// Lawrence Bhai copy kar rahe ho toh credit dena mat bhulna (-_-) (-_-) (-_-) i am Watching

const { Router } = require("express");
const routes = Router();
const UserModel = require("../models/User");
const fs = require("fs");

routes.get("/userInfo", async (req, res) => {
  let queries = req.query;
  // Making an array for $and command
  let andQueryArray = [];
  for (const [key, value] of Object.entries(queries)) {
    let queryObj = {};
    queryObj[key] = value;
    andQueryArray.push(queryObj);
  }
  // Attaching $and command and its array if any quries were provided
  let findObj = {};
  if (andQueryArray.length != 0) {
    findObj[$and] = andQueryArray;
  }
  let db_response = await UserModel.find(findObj);
  res.send(db_response);
});

routes.post("/userInfo", async (req, res) => {
  let userObj = req.body;
  // Generating id using a count stored on the server
  let newId = Number(fs.readFileSync("count.txt", "utf-8")) + 1;
  fs.writeFileSync("count.txt", String(newId));
  userObj.id = newId;
  let response = await UserModel.create(req.body);
  res.json(response);
});

module.exports = routes;
