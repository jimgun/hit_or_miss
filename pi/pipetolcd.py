#!/usr/bin/python

from display import Display
import sys
import time



    
if __name__ == "__main__":
    display = Display()
    k = 0
    try:
        buff = ''
        while True:
            buff += sys.stdin.read(1)
            if buff.endswith('\n'):
                display.printLine(k%4, buff[:-1])
                print buff[:-1]
                buff = ''
                k = k + 1
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass
        
print k