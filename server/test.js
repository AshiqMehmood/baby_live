const { spawn } = require('child_process');

//const logOutput = (name) => (data) => console.log(`${data}`);


function run() {
 const process = spawn('python3', ['../../code.py']);
 const value = process.stdout.on('data', function (data) {
  console.log('>>', data.toString());
  return data.toString();
 }
 );

process.on('close', (code) => {
  console.log(`closed ${code}`)
 });


 return value;

}

module.exports = run;
