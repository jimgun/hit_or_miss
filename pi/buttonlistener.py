#!/usr/bin/python
import RPi.GPIO as GPIO
from threading import Thread
import time
import Queue

class ButtonListener:
    
    def sampleThread( self ):
        while self._listen:
            time.sleep(0.1)
            state = GPIO.input(self._buttonPin)
            #print state
            if state == 0 and self._pressed == False:
                #print "send button pressed message"
                buttonEvent = ButtonPressedEvent(self._buttonPin, self._pressed)
                self._buttonStateEvents.put(buttonEvent)
                self._pressed = True
            if state == 1 and self._pressed == True:
                self._pressed = False
            
    
    def __init__(self, buttonPin=12):
        self._buttonPin = buttonPin
        self._pressed = False;
        self._listen = False
        self._buttonStateEvents = Queue.Queue(maxsize=0)
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._buttonPin, GPIO.IN)

    def start( self ):
    
        self._listen = True
        t = Thread(target=self.sampleThread)
        t.daemon = True
        t.start()
        
        
            
            
    def stop( self ):
        self._listen = False

    def getEventQueue( self ):
        return self._buttonStateEvents
    
    def toString( self ):
        return "button(%d): %d" % (self._buttonPin, self._pressed)

class ButtonPressedEvent:
    def __init__(self, buttonId, buttonState):
        self._id = buttonId
        self._state = buttonState

 
 
#Unit testing below!
 
class TestClass:
    def __init__(self, buttonlistener):
        self.buttonStateEventQueue = buttonlistener.getEventQueue()
        t = Thread(target=self.readEventThread)
        t.daemon = True
        t.start()
        
    def readEventThread(self):
        while True:
            e = self.buttonStateEventQueue.get()
            print "got keypressed: id=%s, state=%s" % (e._id, e._state)
            
if __name__ == "__main__":
    button = ButtonListener(12)
    button.start()
    
    tester = TestClass(button)
    
    raw_input("listening to button. hit enter to exit")
    
    button.stop()