#!/usr/bin/python

from samplestore import SampleStore
import singletons
from sample import Sample
import web

class WebApp:

    def __init__(self, samplestore):
        self._sampleStore = samplestore
        

    def start(self):
        urls =(
            '/last', '_lastSample',
            '/last/([0-9]+)', '_lastSamples',
            '/lcd', '_lcd' 
           
        )
        self._app = web.application(urls, globals())
        self._app.run()

        
class _lastSample:
        def GET(self):
            return singletons.samplestore.getLastSample().toJson()   

class _lastSamples:
        def GET(self, number):
            return singletons.samplestore.toJson(g_webapp_samplestore.getLastSamples(int(number)))
            
class _lcd:
        def GET(self):
            render = web.template.render('templates')
            return render.lcd(singletons.uicontroller.getActivePage()._displayLines[0],
            singletons.uicontroller.getActivePage()._displayLines[1],
            singletons.uicontroller.getActivePage()._displayLines[2],
            singletons.uicontroller.getActivePage()._displayLines[3])
            
        
if __name__ == "__main__":
    store = SampleStore(30)
    singletons.samplestore = store
    for i in range(1,15):
        sample = Sample( 100+i, i )
        store.addSample( sample )
    for i in range(1,15):
        sample = Sample( 100+15+i, 30-i )
        store.addSample( sample )
    webapp = WebApp(store)
    webapp.start()


