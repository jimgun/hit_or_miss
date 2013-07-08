#!/usr/bin/python
from display import Display
from menupage import MenuPage
import os

class CpuTempPage(MenuPage):
    def __init__( self, display ):
        MenuPage.__init__(self,display)
    
    def show( self ):
        MenuPage.show( self )
        self._displayLines[2] = "CPU: " + getCPUtemperature() + "'C";
        self._updateLine(2)

 

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
#Unit tests below! 
        
if __name__ == '__main__':
    display = Display()
    
    menupage = MenuPage(display)
    menupage.show()
    
    raw_input("...")
    
    debugpage = CpuTempPage(display)
    debugpage.show()
    
    raw_input("done!");