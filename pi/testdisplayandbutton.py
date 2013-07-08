#!/usr/bin/python
from buttonlistener import  ButtonListener
from display import Display

from threading import Thread
import time
import Queue
import os 

class FakeDisplayController:

    def __init__(self, buttonlistener, display):
        self.buttonStateEventQueue = buttonlistener.getEventQueue()
        self._display = display
        self._line = 0
        t = Thread(target=self.readEventThread)
        t.daemon = True
        t.start()
        
    def readEventThread(self):
        while True:
            e = self.buttonStateEventQueue.get()
            self._display.printLine(self._line, "")
            self._line = (self._line+1) % 4
            
            self._display.printLine(self._line,"CPU: " + getCPUtemperature() + "'C" )
  


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
    
if __name__ == "__main__":
    button = ButtonListener(12)
    display = Display()
    controller = FakeDisplayController( button, display)
    
    button.start()
    
    raw_input("listening to button. hit enter to exit")
    
    button.stop()