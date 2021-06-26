const express = require('express');
const http = require('http');
const app = express();
const server = http.createServer(app);
const cors = require('cors');
app.use(cors());
//app.use(express.json());
//app.use(express.urlencoded({ extended: false }));
//app.options('*', cors());

//serial port reader
const raspi = require('raspi');
const Serial = require('raspi-serial').Serial;
 
const StringDecoder = require('string_decoder').StringDecoder;
const decoder = new StringDecoder('utf8');
raspi.init(() => {
  const serial = new Serial({ 
   portId: "/dev/ttyACM0",
   baudRate: 9600
});

app.get("/sensors", (req, res) => {
  serial.open(() => {
    serial.on('data', (data) => {
    const buf = decoder.write(data); 
     let val = {};
     val.moisture = buf;
     res.json(val);
     //process.stdout.write(data);
    });
    //serial.write('Hello from raspi-serial');
   });
 });

});

const sensorData = {};


app.get('/', (req, res) => {
 res.send("Baby Monitor Server");
});


const port = process.env.PORT || 3333

server.listen(port, () => {
 console.log(`listening on ${port}`)
});

