const express = require('express');
const http = require('http');
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server);
const CORS = require('cors');

app.get('/', (req, res) => {
 res.send("Baby Monitor Server");
});

app.use(CORS);


io.on('connection', (socket) => {
 console.log('user connected');
});


const port = process.env.PORT || 3000

server.listen(port, () => {
 console.log(`listening on ${port}`)
});

