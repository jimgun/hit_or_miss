#!/usr/bin/python
from display import Display

class MenuPage:
    def __init__( self, display, name = ""):
        self._display = display
        self._name = name
        self._isActive = False
        self._displayLines = [" "," "," "," "]
        

        
    def show( self ):
        self._isActive = True
        self._display.clear()
        #self._display.printLine(0, "MenuPage %s" % self._name)
        
    def hide( self ):
        self._isActive = False
    
    def onPeriodicUpdate( self ):
        if self._isActive == True:
            self._update()
    
    def _update( self ):
        return;
    
    def _updateLine( self, index ):
        self._display.printLine(index, self._displayLines[index])
        return;
        
    def toString( self ):
        retVal = ""
        for str in self._displayLines:
            retVal = retVal + str + "\n"
        return retVal

#Unit tests below! 
        
class DebugPageA(MenuPage):
    def __init__( self, display ):
        MenuPage.__init__(self,display)
    
    def show( self ):
        self._display.clear()
        self._display.printLine(1, "DebugPage1 sub");
        
       
    
if __name__ == '__main__':
    display = Display()
    
    menupage = MenuPage(display)
    menupage.show()
    
    raw_input("...")
    
    debugpage = DebugPageA(display)
    debugpage.show()
    
    raw_input("done!");