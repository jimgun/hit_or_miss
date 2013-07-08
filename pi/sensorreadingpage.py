#!/usr/bin/python
from display import Display
from menupage import MenuPage

class SensorReadingPage(MenuPage):
    def __init__( self, display, sensors ):
        MenuPage.__init__(self,display)
        self._sensors = sensors
    
    def show( self ):
        MenuPage.show( self )
        
        
        line0 = " s%d 0x00   s%d 0x00  " % (self._sensors[0], self._sensors[1] )
        line1 = " s%d 0x00   s%d 0x00  " % (self._sensors[2], self._sensors[3] )
        line2 = " s%d 0x00   s%d 0x00  " % (self._sensors[4], self._sensors[5] )
        line3 = " s%d 0x00   s%d 0x00  " % (self._sensors[6], self._sensors[7] )
        
        self._displayLines = [line0, line1, line2, line3]
        
        self._updateLine(0)
        self._updateLine(1)
        self._updateLine(2)
        self._updateLine(3)

    def _update( self ):
        return;
 

    
#Unit tests below! 
        
#if __name__ == '__main__':
    