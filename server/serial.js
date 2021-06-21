const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline');

const port = new SerialPort('/dev/ttyACM0', {
  baudRate: 9600,
  
});

const parser = port.pipe(new Readline());

port.on("open", () => {
 console.log('open');
 parser.on('data', (data) => {
  console.log(data);
 });
});

