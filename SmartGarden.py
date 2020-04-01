import RPi.GPIO as GPIO
import Adafruit_DHT
import lcdlib
import sys
import time
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

while True:
        lcd = lcdlib.lcd()
        hum, temp = Adafruit_DHT.read_retry(11,14)

        if hum is not None and temp is not None:
                print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temp,hum))
                lcd.lcd_display_string("Temp = {0:0.1f}*C".format(temp),1)
                lcd.lcd_display_string("Humidity = {0:0.1f}%".format(hum),2)
                time.sleep(3)
		print(time.strftime("%d/%m/%Y"),1)
		print(time.strftime("%H:%M:%S"),2)
		time.sleep(2)
	else:
                print("Error....plese try again!")


	if(GPIO.input(7)==1):
		print("Low Light")
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(12,GPIO.LOW)
  
        else:
		print("Brightly")
                GPIO.output(12,GPIO.HIGH)
                GPIO.output(11,GPIO.LOW)


	if(GPIO.input(10)==0):
                print("Water Detected")
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(16,GPIO.LOW)
        else:
		print("Water not detected")
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(15,GPIO.LOW)
