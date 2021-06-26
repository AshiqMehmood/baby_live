import RPi.GPIO as GPIO
from time import sleep


LIGHT_PIN = 4

class Light(object):
 
 def setup(self):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LIGHT_PIN, GPIO.OUT)

 def turnOn(self):
  GPIO.output(LIGHT_PIN, GPIO.HIGH)
  print('Light ON')
  sleep(10)


 def turnOff(self):
  GPIO.output(LIGHT_PIN, GPIO.LOW)
  sleep(3)

 def destroy(self):
  GPIO.cleanup()

#if __name__ == '__main__':     # Program start from here
 #l = Light()
 #l.setup()
 #try:
 # l.turn_on()
 #except KeyboardInterrupt:
 # l.destroy()
