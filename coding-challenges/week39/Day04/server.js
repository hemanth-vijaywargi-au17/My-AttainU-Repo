// Dependencies
const express = require("express");
const { buildSchema } = require("graphql"); // GraphQL an Alternative to REST API
const { graphqlHTTP } = require("express-graphql"); // To Use graphql with express
const { default: axios } = require("axios");

// Creating an Express Server
const app = express();
const PORT = 3000;

// Creating GraphQl Schema
const MyGraphQLSchema = buildSchema(`
    type Query{
        random_even_number : Int,
        random_odd_number : Int,
        random_joke : String
    }
`);

// Resolvers
const rootResolvers = {
  random_even_number: () => {
    let number = Math.floor(Math.random() * 100);
    return number % 2 === 0 ? number : number + 1;
  },
  random_odd_number: () => {
    let number = Math.floor(Math.random() * 100);
    return number % 2 === 0 ? number + 1 : number;
  },
  random_joke: async () => {
    let { data: { value } } = await axios.get("https://api.chucknorris.io/jokes/random");
    return value;
  },
};

// Using graphl with express
app.use(
  "/graphql",
  graphqlHTTP({
    schema: MyGraphQLSchema,
    rootValue: rootResolvers,
    graphiql: true, // Use GraphQL's Graphical Interface in the browser
  })
);

// Starting the Server
app.listen(PORT, () => {
  console.log(`Server Running at PORT : ${PORT}`);
});
