import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

try:
    while True:
        GPIO.output(7,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(7,GPIO.LOW)
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

    
