const express = require("express");
const axios = require("axios");
const app = express();
const port = 3000;

app.get("/postWithComment", async (req, res) => {
  let response = await axios.get("https://jsonplaceholder.typicode.com/posts");
  let posts = response.data;

  let promisesArray = posts.map((post) => {
    return axios.get(
      `https://jsonplaceholder.typicode.com/comments?postId=${post.id}`
    );
  });
  let responsesArray = await Promise.all(promisesArray);

  responsesArray.forEach((response, index) => {
    posts[index].comments = response.data;
  });

  res.send(posts);
});

app.listen(port, () => {
  console.log(`Server running at port : ${port}!`);
});
