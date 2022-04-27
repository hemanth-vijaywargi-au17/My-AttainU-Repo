// Dependencies
const express = require("express");
const { WebSocketServer } = require("ws");

// Express Server
const app = express();
const PORT = 5000;

// Route
app.get("/", (req, res) => {
  res.sendFile(`${__dirname}/index.html`);
});

// Starting the Express Server
app.listen(PORT, () => {
  console.log(`Express Server Running at PORT : ${PORT}`);
});

// Web Socket Server
const wsServer = new WebSocketServer({ port: 5001 });
let count = 0

// Creating a function which broadcasts a message to all Connected Clients 
wsServer.broadcast = function (data) {
  wsServer.clients.forEach((client) => client.send(data));
};

// On Successful Connection/Handshake to a Client
wsServer.on("connection", (ws) => {
  ws.send(String(count));

  // Logging client IP Address
  let clientIP = ws._socket.remoteAddress;
  console.log(
    `Connected to Client ${clientIP}`
  );

  // On Closing of Connection from a Client
  ws.on("close", () => {
    console.log(`Disconnected from Client ${clientIP}`);
  });

  // On Message Recevied from a Client
  ws.on("message", (message) => {
    if (String(message) === "increment") {
      count += 1;
      wsServer.broadcast(String(count));
    }
  });
});
