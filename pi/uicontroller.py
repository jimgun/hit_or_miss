#!/usr/bin/python
from buttonlistener import ButtonListener
from display import Display
import Queue
from threading import Thread

from menupage import MenuPage
from cputemppage import CpuTempPage
from systeminfopage import SystemInfoPage
from sensorinfopage import SensorInfoPage
from connectioninfopage import ConnectionInfoPage
from sensorreadingpage import SensorReadingPage
import time

class UiController:
    
    def __init__(self, buttonlistener, display, doPeriodic=False, interval = 1):
        self.buttonStateEventQueue = buttonlistener.getEventQueue()
        self._display = display
        self._menuPages = []
        self._currentPage = 0;
        self._doPeriodic = doPeriodic
        self._interval = interval
        
        t = Thread(target=self.readEventThread)
        t.daemon = True
        t.start()
    
        self._addPages()
        self.setActivePage(0)
        
        if doPeriodic == True:
            t = Thread(target=self._onPeriodicUpdate)
            t.daemon = True
            t.start()
        
    def _onPeriodicUpdate( self ):
        while True:
            for page in self._menuPages:
                page.onPeriodicUpdate()
            time.sleep(self._interval)
        return
    
    def _addPages( self ):
        self._menuPages.append(SystemInfoPage(self._display))
        self._menuPages.append(SensorInfoPage(self._display))
        self._menuPages.append(ConnectionInfoPage(self._display))
        self._menuPages.append(SensorReadingPage(self._display, [1,2,3,4,5,6,7,8]))
        self._menuPages.append(CpuTempPage(self._display))


        
    
    
    def readEventThread(self):
        while True:
            e = self.buttonStateEventQueue.get()
            self._menuPages[self._currentPage].hide()
            self._currentPage = (self._currentPage +1) % len(self._menuPages);
            self._menuPages[self._currentPage].show()
    
    
    def setActivePage(self,index):
        self._currentPage = index
        for i, page in enumerate(self._menuPages):
            if i != index:
                page.hide()
            else:
                page.show()
    
    def getActivePage(self):
        return self._menuPages[self._currentPage]
    
#Unit tests below!

if __name__ == "__main__":
    
    button = ButtonListener()
    button.start()
    display = Display()
    
    ui = UiController(button, display)
    
    raw_input("menu up! press button...")