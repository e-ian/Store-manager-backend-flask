import unittest
from api.v1 import app
from tests import(create_admin, create_attendant, create_product, create_sale, login_admin)
from api.v1 import views
from api.v1.db_actions import Products, Sales
import json
from config import Testingconfig
from api.v1.models import Datastore

app.config.from_object(Testingconfig)

db = Datastore()

class TestUser(unittest.TestCase):
    def setUp(self):

        self.client = app.test_client()
        db.create_products_table()
        db.create_sales_table()
        db.create_user_table()

    def tearDown(self):
        drop_users = "DROP TABLE users CASCADE"
        db.cur.execute(drop_users)
        drop_products = "DROP TABLE products CASCADE"
        db.cur.execute(drop_products)
        drop_sales = "DROP TABLE sales CASCADE"
        db.cur.execute(drop_sales)

    def signup_user(self, register_user):
        response = self.client.post("/api/v1/auth/signup", \
        data = json.dumps(register_user), content_type = 'application/json')
        return response

    def signin_user(self, login_admin):
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_admin), content_type = 'application/json')
        token = response.json
        return token

    def add_a_product(self, create_product):
        response = self.client.post("/api/v1/products", headers={'Authorization':'Bearer '+self.signin_user(login_admin)}, data=json.dumps(create_product), content_type='application/json')
        return response
        