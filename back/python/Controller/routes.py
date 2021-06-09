from Model.auth import *

def setuproute(app, call):
    @app.route('/',                             ['OPTIONS', 'GET'],         lambda x = None: call([])) #done
    def base():
        return
