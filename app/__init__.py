from flask import Flask
import config
from app.logger import log

class App():
    """
    App class creates multiple objects that this Python application will require and maintains them in wrapper class.
    config : Config class from config.py
    flask_app : The Flask application
    """
    def __create_config(self):
        """
        Creates config object and determines config subclass based on environment.
        """
        app_config = config.Config()

        if app_config.SERVER_HOST_NAME !=  "dev_server":
            app_config = config.ProductionConfig()
        else :
            app_config = config.DevelopmentConfig()

        return app_config

    def __create_app(self):
        """
        Creates a new flask application
        """
        flask_app = Flask(__name__)
        flask_app.config.from_object(self.config) #sets application default settings
        return flask_app

    def __init__(self):
        """
        call methods to initialize objects
        """
        self.config = self.__create_config()
        self.flask_app = self.__create_app()

def init_app():
    """ Create a new App object """
    log('app.init.py')
    return App()

app = init_app()
config = app.config 
flask_app = app.flask_app



from app import views

