import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import os
from time import sleep

LIGHT_PIN = 4

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(LIGHT_PIN, GPIO.OUT)


while True: # Run forever
    if GPIO.input(16) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
        os.system('lsof -t -i:5000') #kill all port
        sleep(1)
        os.system('python3 main.py')
        sleep(10)
    else:
        print('No action')
        GPIO.output(LIGHT_PIN, GPIO.LOW)
