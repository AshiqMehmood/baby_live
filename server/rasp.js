const raspi = require('raspi');
const Serial = require('raspi-serial').Serial;
 
const StringDecoder = require('string_decoder').StringDecoder;
const decoder = new StringDecoder('utf8');

function  serialMonitor() {
raspi.init(() => {
  const serial = new Serial({ 
   portId: "/dev/ttyACM0",
   baudRate: 9600
});
  serial.open(() => {
    serial.on('data', (data) => {
    const buf = decoder.write(data); 
     return buf;

     //process.stdout.write(data);
    });
    //serial.write('Hello from raspi-serial');
  });
});

}
module.exports = serialMonitor
