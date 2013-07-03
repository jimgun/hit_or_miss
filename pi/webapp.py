#!/usr/bin/python

from samplestore import SampleStore
from sample import Sample
import web

class WebApp:

    def __init__(self, samplestore):
        self._sampleStore = samplestore
        

    def start(self):
        urls =(
            '/last', '_lastSample',
            '/last/([0-9]+)', '_lastSamples'
        )
        self._app = web.application(urls, globals())
        self._app.run()

        
class _lastSample:
        def GET(self):
            return g_webapp_samplestore.getLastSample().toJson()   

class _lastSamples:
        def GET(self, number):
            return g_webapp_samplestore.toJson(g_webapp_samplestore.getLastSamples(int(number)))
        
if __name__ == "__main__":
    store = SampleStore(30)
    g_webapp_samplestore = store #dirty!
    for i in range(1,15):
        sample = Sample( 100+i, i )
        store.addSample( sample )
    for i in range(1,15):
        sample = Sample( 100+15+i, 30-i )
        store.addSample( sample )
    webapp = WebApp(store)
    webapp.start()


