// Dependencies
const express = require("express");
const { createServer } = require("http");
const { Server } = require("socket.io");

// Creating an Express Server
const app = express();
const PORT = process.env.PORT || 5000;

// Get the underlying http Server Instance from express app
const httpServer = createServer(app);

// Creating WebSocket Server using http Server Instance (in-order to share the same port)
const io = new Server(httpServer);

// Whenever someone connects this gets executed
io.on("connection", function (socket) {
  console.log("A user connected");

  // Whenever someone disconnects this piece of code executed
  socket.on("disconnect", function () {
    console.log("A user disconnected");
  });

  socket.on("userInput", function (value) {
    socket.broadcast.emit('otherUserInput',value)
  });
});

// Route
app.get("/", (req, res) => {
  res.sendFile(`${__dirname}/views/index.html`);
});

// Starting the Express Server
httpServer.listen(PORT, () => {
  console.log(`HTTP Server Listening at PORT : ${PORT}`);
});
