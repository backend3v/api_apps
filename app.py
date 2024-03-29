from flask import Flask

from aplication.api.user_routes import UserRoutes
from aplication.api.resource_routes import ResourceRoutes
from aplication.views.home_routes import HomeRoutes 
from aplication.views.app_english_routes import AppEnRoutes 
from aplication.api.test import TestRoutes
from config import Config
from flask_cors import CORS


app = Flask(__name__,template_folder='aplication/templates')
class Application:
    def __init__(self):
        #self.app = Flask(__name__,template_folder='aplication/templates')
        CORS(app)
        app.config['SECRET_KEY'] = Config().secret_app
        UserRoutes(app)
        ResourceRoutes(app)
        HomeRoutes(app)
        AppEnRoutes(app)
        TestRoutes(app)
    def runner(self):
        app.run(host=Config().host, port=Config().port,
                     debug=Config().debu)

def run_app():
    aplication = Application()
    return aplication.app
if __name__ == '__main__':
    aplication = Application()
    aplication.runner()
