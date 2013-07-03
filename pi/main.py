#!/usr/bin/python
from samplestore import SampleStore
from webapp import WebApp



if __name__ == "__main__":
    #create all objects
    
    store = SampleStore(599)
    g_webapp_samplestore = store
    
    webapp = WebApp( store )
    
    #start the show!    
    webapp.start()
    
    print store.toString()
