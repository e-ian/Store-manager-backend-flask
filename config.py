"""module to configure database"""
import os

class Config(object):
    """super config class"""
    DEBUG = False
    dbname = "Storemanagerdb"

class DevelopmentConfig(Config):
    """class for development config"""
    DEBUG = True

class Testingconfig(Config):
    """class for testing config"""
    DEBUG = False
    TESTING = True