#!/usr/bin/python
from samplestore import SampleStore
from webapp import WebApp
from buttonlistener import ButtonListener
from uicontroller import UiController
from display import Display
import RPi.GPIO as GPIO
import singletons

IO_BUTTON = 12
pinE  = 5
pinRs = 3
pinD4 = 7
pinD5 = 11
pinD6 = 13
pinD7 = 15


def initGpio():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IO_BUTTON, GPIO.IN)
    
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

def cleanupGpio():
    print "cleaning up!"
    GPIO.cleanup()
    
if __name__ == "__main__":
    
    
    try:
    
        initGpio()
        
        #create all objects
        
        button = ButtonListener(IO_BUTTON)
        button.start()
        display = Display()
        
        ui = UiController(button, display, True, 1)
        
        #raw_input("menu up! press button...")
        
        store = SampleStore(599)
        singletons.samplestore = store
        singletons.uicontroller = ui
        
        #test
        # for i in range(1,15):
            # sample = Sample( 100+i, i )
            # store.addSample( sample )
        # for i in range(1,15):
            # sample = Sample( 100+15+i, 30-i )
            # store.addSample( sample )
        #
        
        webapp = WebApp( store )
        
        #start the show!    
        webapp.start()
    
    
    except KeyboardInterrupt:
        cleanupGpio()
      
    
    