import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 14
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, True)
