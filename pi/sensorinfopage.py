#!/usr/bin/python
from display import Display
from menupage import MenuPage

class SensorInfoPage(MenuPage):
    def __init__( self, display ):
        MenuPage.__init__(self,display)
    
    def show( self ):
        MenuPage.show( self )
        line0 = " "
        line1 = "  1 2 3 4 5 6 7 8   "
        line2 = "  - - * - - - * -   "
        line3 = " "
        
        self._displayLines = [line0, line1, line2, line3]
        
        self._updateLine(0)
        self._updateLine(1)
        self._updateLine(2)
        self._updateLine(3)

    def _update( self ):
        return;
 

    
#Unit tests below! 
        
#if __name__ == '__main__':
    