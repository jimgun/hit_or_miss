#!/usr/bin/python


#import
import RPi.GPIO as GPIO
import time
BUTTON1 = 12

def main():
    buttonPressed = False
    GPIO.setmode(GPIO.BOARD)       # Use BOARD GPIO numbers
    GPIO.setup(BUTTON1, GPIO.IN)  # 
    while True:
        state = GPIO.input(BUTTON1)
        #print state
        if state == 0 and buttonPressed == False:
            print "send button pressed message"
            buttonPressed = True
        if state == 1 and buttonPressed == True:
            buttonPressed = False
            
        time.sleep(0.01)
    
   


if __name__ == '__main__':
    main()