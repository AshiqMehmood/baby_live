from flask import Flask, jsonify, request
from flask_cors import CORS
import serial
import time
import json
import motor
import light

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
 msg = 'connected'
 return jsonify({"message": msg})


#serial-reading
#ser = serial.Serial('/dev/ttyACM0', 9600)


@app.route('/sensors', methods=['GET'])
def list_data():
   ser= serial.Serial('/dev/ttyACM0',9600)
   read_serial = ser.readline()
   read = read_serial.strip() 
   data_to_json = json.loads(read)
   #print(data)
   return jsonify(data_to_json)

@app.route('/drive', methods=['GET'])
def run_motor():
  print('motor runninng.....')
  action = request.args.get('action')
  if action.lower() == 'on':
   print('Motor turned ON')
   m = motor.MotorDrive('on')
   m.setup()
   m.run()
   #m.destroy()

  elif action.lower() == 'off':
   m = motor.MotorDrive(action)
   m.setup()
   m.stop()
   print('Motor switched OFF')
   m.destroy()

  return "OK"


@app.route('/fan', methods=['GET'])
def control_fan():
  print('fan running.....')
  action = request.args.get('action')
  if action.lower() == 'on':
   print('Fan turned ON')
   m = motor.MotorDrive('on')
   m.setup()
   m.turnOnFan()
   #m.destroy()

  elif action.lower() == 'off':
   m = motor.MotorDrive(action)
   m.setup()
   m.stop()
   print('Fan switched OFF')
   m.destroy()

  return "OK"


@app.route('/light', methods=['GET'])
def control_light():
  print('Light is ON')
  action = request.args.get('action')
  l = light.Light()
  if action.lower() == 'on':
   l.setup()
   l.turnOn()
   print('Light swithced ON')
  elif action.lower() == 'off':
   l.setup()
   l.turnOff()
   print('Light switched OFF')
   l.destroy()
  return "OK"


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)



