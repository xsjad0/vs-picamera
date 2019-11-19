import os
import cherrypy
from time import sleep
from picamera import PiCamera

static_dir = os.path.abspath(os.getcwd())
image_dir = static_dir + '/public/images/'
image_default_name = 'shot.jpg'
web_dir = static_dir + '/public/'

class CameraRoot():
    @cherrypy.expose
    def index(self):
        return open(web_dir + 'index.html')

@cherrypy.expose
class CameraWebService():

    def __init__(self):
        pass

    def GET(self):
        return image_default_name

    def POST(self):
        with PiCamera() as camera:
            camera.capture(image_dir + image_default_name)

    def DELETE(self):
        os.remove(image_dir + image_default_name)


if __name__ == "__main__":
    conf = {
        '/': {
            'tools.staticdir.root': static_dir
        },
        '/api': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0'}
    )
    webapp = CameraRoot()
    webapp.api = CameraWebService()
    cherrypy.quickstart(webapp, '/', conf)
