"""
This is configuration file for application 
"""
import os
from configparser import ConfigParser



class Config():
    """
    This is base config
    """
    DEBUG = False
    TESTING = False
    USER_RELOADER = False
    CSRF_ENABLED = True
    SECRET_KEY = "sddfdgheadfsdfgfhukkjbfgdcvh".encode('utf-8') #Randomly type any string for each application
    SESSION_COOKIE_NAME = "session_currencyapis" #change this depending on application
    SERVER_HOST_NAME = "dev_server"

    def __init__(self):
        """ When config file is initialized, it will attempt to read config.ini for api key"""
        config = ConfigParser()
        config_exist = os.path.isfile('config.ini')

        if config_exist :
            config.read('config.ini')
            self.API_KEY = config['DEFAULT']['API_KEY']
        else:
            raise IOError

class ProductionConfig(Config):
    """ The production config """
    DEBUG = False
    USER_RELOADER = False

class DevelopmentConfig(Config):
    """ The development config """
    DEVELOPMENT = True
    DEBUG = True
    USER_RELOADER = True
