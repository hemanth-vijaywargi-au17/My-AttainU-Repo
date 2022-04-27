const express = require("express");
const fs = require("fs");
const app = express();
const port = 3000;

// Using ejs template engine
app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: true }));

app.get("/dogform", (req, res) => {
  res.render("DogForm");
});

app.post("/formSubmit", (req, res) => {
  // Stringifying and Writing incoming data to json file
  let data = req.body
  let stringifiedData = JSON.stringify(data);
  fs.writeFileSync("data.json", stringifiedData);

  // Rendering the data using template engine
  res.render("DogInfo", data);
});

app.listen(port, () => {
  console.log(`Server Running at Port : ${port}!`);
});
