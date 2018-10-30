"""module to run flask app"""
from api.v1.models import Datastore
from flask import Flask

from api.v1 import app

# app = Flask(__name__)
# from api.v1.views import views

if __name__ == '__main__':
    db_connect = Datastore()
    db_connect.create_user_table()
    db_connect.create_products_table()
    db_connect.create_sales_table()
    app.run(debug=True)
