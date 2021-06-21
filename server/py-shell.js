const {PythonShell} = require('python-shell');

function runShell() {
const readings = {};

let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
  //scriptPath: '',
  //args: ['value1', 'value2', 'value3']
};

PythonShell.run('../../code.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
   console.log('results: %j', results);
   //readings.data = results;
});

//return readings;
}

runShell();

//module.exports = runShell;
