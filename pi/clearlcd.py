#!/usr/bin/python
import RPi.GPIO as GPIO
from display import Display
import time

pinE  = 5
pinRs = 3
pinD4 = 7
pinD5 = 11
pinD6 = 13
pinD7 = 15

if __name__ == "__main__":
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pinE, GPIO.OUT)  # E
    GPIO.setup(pinRs, GPIO.OUT) # RS
    GPIO.setup(pinD4, GPIO.OUT) # DB4
    GPIO.setup(pinD5, GPIO.OUT) # DB5
    GPIO.setup(pinD6, GPIO.OUT) # DB6
    GPIO.setup(pinD7, GPIO.OUT) # DB7
    
    GPIO.output(pinE, False)
    GPIO.output(pinRs, False)
    GPIO.output(pinD4, False)
    GPIO.output(pinD4, False)
    GPIO.output(pinD4, False)
    GPIO.output(pinD4, False)
    

    display = Display()
    display.clear()
    #display.printLine(0, "--------------------")
    #display.printLine(1, "                    ")
    display.printLine(2, "       starting     ")
    #display.printLine(3, "--------------------")
    
    for i in range(0,4):
        symbol = ""
        for j in range(0,i):
            symbol = symbol + "."
        str = "       starting " + symbol
        display.printLine(2,str)
        time.sleep(1)
    
    GPIO.cleanup()


