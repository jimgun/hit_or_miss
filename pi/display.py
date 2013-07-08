#!/usr/bin/python


#import
import RPi.GPIO as GPIO
import time
import socket

# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

class Display:
    def __init__( self, pinRs=3, pinE=5, pinD4=7, pinD5=11, pinD6=13, pinD7=15 ):
        self._pinRs = pinRs
        self._pinE = pinE
        self._pinD4 = pinD4
        self._pinD5 = pinD5
        self._pinD6 = pinD6
        self._pinD7 = pinD7

        
        GPIO.setmode(GPIO.BOARD)    # Use BOARD GPIO numbers
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

        self._lcdInit()
        
    def _lcdInit( self ):
        # Initialise display
        self._lcdByte(0x33,LCD_CMD)
        self._lcdByte(0x32,LCD_CMD)
        self._lcdByte(0x28,LCD_CMD)
        self._lcdByte(0x0C,LCD_CMD)  
        self._lcdByte(0x06,LCD_CMD)
        self._lcdByte(0x01,LCD_CMD)  
    
    def _lcdString(self, message):
        # Send string to display
    
        message = message.ljust(LCD_WIDTH," ")  
    
        for i in range(LCD_WIDTH):
            self._lcdByte(ord(message[i]),LCD_CHR)

    def _lcdByte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = True  for character
        #        False for command

        GPIO.output(self._pinRs, mode) # RS

        # High bits
        GPIO.output(self._pinD4, False)
        GPIO.output(self._pinD5, False)
        GPIO.output(self._pinD6, False)
        GPIO.output(self._pinD7, False)
        if bits&0x10==0x10:
            GPIO.output(self._pinD4, True)
        if bits&0x20==0x20:
            GPIO.output(self._pinD5, True)
        if bits&0x40==0x40:
            GPIO.output(self._pinD6, True)
        if bits&0x80==0x80:
            GPIO.output(self._pinD7, True)

        # Toggle 'Enable' pin
        time.sleep(E_DELAY)    
        GPIO.output(self._pinE, True)  
        time.sleep(E_PULSE)
        GPIO.output(self._pinE, False)  
        time.sleep(E_DELAY)      

        # Low bits
        GPIO.output(self._pinD4, False)
        GPIO.output(self._pinD5, False)
        GPIO.output(self._pinD6, False)
        GPIO.output(self._pinD7, False)
        if bits&0x01==0x01:
            GPIO.output(self._pinD4, True)
        if bits&0x02==0x02:
            GPIO.output(self._pinD5, True)
        if bits&0x04==0x04:
            GPIO.output(self._pinD6, True)
        if bits&0x08==0x08:
            GPIO.output(self._pinD7, True)

        # Toggle 'Enable' pin
        time.sleep(E_DELAY)    
        GPIO.output(self._pinE, True)  
        time.sleep(E_PULSE)
        GPIO.output(self._pinE, False)  
        time.sleep(E_DELAY)       
    
    def _lineNumer2LcdLine(self, lineNumber):
        return {
            0: LCD_LINE_1,
            1: LCD_LINE_2,
            2: LCD_LINE_3,
            3: LCD_LINE_4
        }[lineNumber]
    
    def printLine(self, lineNumber, lineContent):
        line = self._lineNumer2LcdLine(lineNumber)
        self._lcdByte(line, LCD_CMD)
        self._lcdString(lineContent)
        
    def clear(self):
        for i in range(0,4):
            self.printLine(i,"")
        
    


#Unit tests below!        
    


if __name__ == '__main__':
    display = Display()
    
    display.printLine(0, "3G " + chr(0xCB))
    display.printLine(1, socket.gethostbyname(socket.gethostname()))
    display.printLine(2, "ABCDEFGHIJKLMNOPQRST")
    display.printLine(3, "abcdefghijklmnopqrst" )
    
    raw_input("done!")