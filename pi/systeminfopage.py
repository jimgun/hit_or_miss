#!/usr/bin/python
from display import Display
from menupage import MenuPage
import os
import netifaces
import psutil

class SystemInfoPage(MenuPage):
    def __init__( self, display ):
        MenuPage.__init__(self,display)
    
    def show( self ):
        MenuPage.show( self )
        line0 = " CPU: " + getCPUtemperature() + "'C   "+getCPULoad()+"%"
        line1 = "Batt: XY.ZV"
        line2 = " MAC: " + getMacAddress("eth0")
        line3 = "  IP: " + getIpAddress("eth0")
        
        self._displayLines = [line0, line1, line2, line3]
        
        self._updateLine(0)
        self._updateLine(1)
        self._updateLine(2)
        self._updateLine(3)

    def _update( self ):
        self._displayLines[0] = " CPU: " + getCPUtemperature() + "'C   "+getCPULoad()+"%"
        self._updateLine(0)
        return;
 

def getCPUtemperature():
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
    
def getMacAddress( ifName ):
    return netifaces.ifaddresses(ifName)[netifaces.AF_LINK][0]['addr'].replace(':', '').upper()
    
def getIpAddress( ifName ):
    return netifaces.ifaddresses(ifName)[netifaces.AF_INET][0]['addr']

def getCPULoad():
    return str(psutil.cpu_percent(interval=0.0))
    
    
#Unit tests below! 
        
if __name__ == '__main__':
    display = Display()
    
    menupage = MenuPage(display)
    menupage.show()
    
    raw_input("...")
    
    debugpage = SystemInfoPage(display)
    debugpage.show()
    
    raw_input("done!");
