"""module to run flask app"""
from api.v1.models import Datastore
from flask import Flask

from api.v1 import app

if __name__ == '__main__':
    
    app.run(debug=True)
