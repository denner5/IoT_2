import drebar
import dbhandler
import RPi.GPIO as GPIO
import time

Button = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button, GPIO.IN)
#GPIO.setwarnings(False)

def butsta():
    while True:
        if GPIO.input(16) == GPIO.HIGH:
            print("ikke trykket")
            #barcode_read()
            #time.sleep(10)
        else:
            print("trykket")
            dbhandler.dbdata.Stregkode = str(drebar.barcode_read())
            dbhandler.control()
        time.sleep(0.5)
butsta()