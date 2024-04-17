# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import RGB1602
import time
import math
colorR = 64
colorG = 128
colorB = 64

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN)

LCD_MOVERIGHT = 0x18
LCD_MOVELEFT = 0x1C

lcd=RGB1602.RGB1602(16,2)

rgbRed = (255,0,0)
rgbGreen = (0,255,0)
rgbBlack = (0,0,0)

scrollDelay = 0.6
scrollCount = 10

arrowsRight = "--> --> --> --> --> --> --> --> --> --> --> --> --> --> --> --> --> --> --> --> "
arrowsLeft =  "<-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- "

while 1==1:
    if GPIO.input(10):
        lcd.setRGB(rgbRed[0],rgbRed[1],rgbRed[2])
        lcd.clear
        lcd.setCursor(0, 0)
        lcd.printout(arrowsLeft)  
        lcd.setCursor(0, 1)
        lcd.printout(arrowsLeft)
        lcd.command(LCD_MOVERIGHT)
        time.sleep(scrollDelay)
    else: 
        lcd.clear
        lcd.setCursor(0, 0)
        lcd.printout(arrowsRight)  
        lcd.setCursor(0, 1)
        lcd.printout(arrowsRight)

        lcd.setRGB(rgbGreen[0],rgbGreen[1],rgbGreen[2])
        lcd.command(LCD_MOVELEFT)
        time.sleep(scrollDelay)

lcd.setRGB(rgbBlack[0],rgbBlack[1],rgbBlack[2])
lcd.clear