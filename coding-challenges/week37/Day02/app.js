// Parsing CSV to JSON

// Module Imports
const fs = require("fs"); // FileSystem
const csvtojson = require("csvtojson"); // CSVtoJSON Parser

// Read Stream (to read from CSV file)
const csvReadStream = fs.createReadStream("train.csv");

// Write Stream (to write to JSON file)
const jsonWriteStream = fs.createWriteStream("train.json");

// Creating an instance of CSV to JSON parser 
const csvParser = csvtojson();

// Seperator is initially an empty String
var seperator = "";

// Writing opening bracket for our JSON Array
jsonWriteStream.write("[", "utf-8");

// Reading --> Parsing --> Writing data in chunks (also writing seperator)
csvReadStream.pipe(csvParser).on("data", (chunk) => {
  jsonWriteStream.write(seperator + chunk, "utf-8");
  // Changing seperator to a comma(,) and a newline character (\n) after the first chunk is written
  if (!seperator) {
    seperator = ",\n";
  }
});

// Writing closing bracket for our JSON Array when csvParser is done parsing the data that it receives
csvParser.on("done", () => {
  jsonWriteStream.write("]", "utf-8");
});
