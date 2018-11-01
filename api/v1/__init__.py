from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api.v1.models import Datastore 


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'akokoro'
jwt = JWTManager(app)
db_connect = Datastore()
db_connect.create_user_table()
db_connect.create_products_table()
db_connect.create_sales_table()
from api.v1.views import views




