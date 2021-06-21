import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 24
Motor1B = 23
Motor1E = 25
FanA = 17
FanB = 27
 
class MotorDrive(object):
 def __init__(self, action):
  self.action = action
 
 def setup(self):
  GPIO.setmode(GPIO.BCM)				# GPIO Numbering
  GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
  GPIO.setup(Motor1B,GPIO.OUT)
  GPIO.setup(Motor1E,GPIO.OUT)
  GPIO.setup(FanA, GPIO.OUT)
  GPIO.setup(FanB, GPIO.OUT)

 def run(self):
 # Going forwards
   GPIO.output(Motor1A,GPIO.HIGH)
   GPIO.output(Motor1B,GPIO.LOW)
   GPIO.output(Motor1E,GPIO.HIGH)
   GPIO.output(FanA,GPIO.LOW)
   GPIO.output(FanB,GPIO.LOW)
   sleep(5)

# Going backwards
 def runBackwards(self): 
  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.HIGH)
  GPIO.output(Motor1E,GPIO.HIGH)
  sleep(5)

 def turnOnFan(self):
  GPIO.output(FanA,GPIO.HIGH)
  GPIO.output(FanB,GPIO.LOW)
  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.LOW)
  sleep(5)

# Stop running motor
 def stop(self):
   GPIO.output(Motor1E,GPIO.LOW)
   GPIO.output(Motor1A, GPIO.LOW)
   GPIO.output(Motor1B, GPIO.LOW)
   GPIO.output(FanA, GPIO.LOW)
   GPIO.output(FanB, GPIO.LOW)

 def destroy(self):	
  GPIO.cleanup()


#if __name__ == '__main__':     # Program start from here
#motor = MotorDrive('off')
 #motor.setup()
 #try:
 # motor.loop()
 #except KeyboardInterrupt:
 # motor.destroy()
