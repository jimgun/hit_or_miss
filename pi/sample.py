#!/usr/bin/python

import time
class Sample:
    
    def __init__(self, timeStamp, data):
        self._timeStamp = timeStamp
        self._data = data




    def toJson(self):
        return "[%s,%s]"  % (self._timeStamp, self._data)
    
    
    def toString(self):
        return "%d sample: %s" % (self._timeStamp, self._data)











if __name__ == "__main__":
    sample = Sample(12345, 321)
    print sample.toString()
    print sample.toJson()