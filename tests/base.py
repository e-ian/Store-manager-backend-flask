import unittest
from api.v1 import app
from tests import(create_admin, create_attendant, create_product, create_sale, \
login_admin, login_attendant, invalid_input_signup, empty_login, empty_signup)
from api.v1.db_actions import Products, Sales
import json
from config import Testingconfig
from api.v1.models import Datastore
import re

app.config.from_object(Testingconfig)

db = Datastore()

class TestUser(unittest.TestCase):
    def setUp(self):

        self.client = app.test_client()
        self.db = Datastore()

    def tearDown(self):
        self.db.cur.execute("DROP TABLE users CASCADE")
        self.db.cur.execute("DROP TABLE products CASCADE")
        self.db.cur.execute("DROP TABLE sales CASCADE")

    def register_admin(self, create_admin):
        response = self.client.post("/api/v1/auth/admin", \
        data = json.dumps(create_admin), content_type = 'application/json')
        return response

    def signin_admin(self, login_admin):
        self.register_admin(create_admin)
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_admin), content_type = 'application/json')
        message = json.loads(response.data.decode())
        # print(message)
        return message["access_token"]

    def signup_user(self, create_attendant):
        self.signin_admin(login_admin)
        response = self.client.post("/api/v1/auth/signup", \
        data = json.dumps(create_attendant), headers={"Authorization":"Bearer "+ str(self.signin_admin(login_admin)), \
        'content_type' : 'application/json'})
        return response

    def signin_attendant(self, login_attendant):
        # self.signup_user(create_attendant)
        response = self.client.post("/api/v1/auth/admin", \
        data = json.dumps(create_admin), content_type = 'application/json')
        response = self.client.post("/api/v1/auth/login", \
        data = json.dumps(login_admin), content_type = "application/json")
        response = self.client.post("/api/v1/auth/signup", \
        data = json.dumps(create_attendant), headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)), \
        'content_type' : 'application/json'})
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_attendant), content_type = 'application/json')
        token = json.loads(response.data.decode())
        print(token)
        return token["access_token"]

    def add_a_product(self, create_product):        
        response = self.client.post("/api/v1/products", data=json.dumps(create_product), \
        headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)), \
        'content_type' : 'application/json'})
        return response

    def add_a_sale(self, create_sale):
        response = self.client.post("/api/v1/sales", data=json.dumps(create_sale), \
        headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response