#!/usr/bin/python
from sample import Sample
class SampleStore:
    
    def __init__(self, maxSamplesInStore):
        self._maxSamples = maxSamplesInStore
        self._sampleList = []
        self._subscribers = []

    def addSample( self, sample ):
        if len(self._sampleList) == self._maxSamples:
            self._sampleList.remove(self._sampleList[0])
        self._sampleList.append( sample )
        self.notifySampleAdded( sample )
        
    def subscribe( self, subscriber ):
        self._subscribers.append( subscriber )

    def unSubscribe( self, subscriber ):
        if subscriber in self._subscribers: self._subscribers.remove(subscriber)
        
    def notifySampleAdded( self, sample ):
        for subscriber in self._subscribers:
            subscriber.onSampleAdded( sample )
    
    def getLastSample( self ):
        return self._sampleList[len(self._sampleList)-1]
        
    def getLastSamples( self, numberOfSamples ):
        return self._sampleList[-numberOfSamples:]
        
    def getNumberOfSamples( self ):
        return len(self._sampleList)
        
    def toJson(self, samples):
        str = "["
        for i,sample in enumerate(samples):
            str += sample.toJson()
            if i < len(samples)-1:
                str += ","
        str += "]"
        return str
    
    
    def toString( self ):
        return "samplestore with numsamples=%d" % len(self._sampleList)









class NotificationTester:
    def onSampleAdded(self, sample ):
        print "-> notified of sample %s" % sample.toString()

if __name__ == "__main__":
    store = SampleStore(10)
    notifications = NotificationTester()
    store.subscribe(notifications)
    for i in range(1,15):
        if i > 8:
            store.unSubscribe(notifications)
        sample = Sample( 100+i, i )
        store.addSample( sample )
        print store.getLastSample().toJson()
        print store.getNumberOfSamples()
    print store.toJson(store.getLastSamples(3))