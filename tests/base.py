import unittest
from api.v1 import app
from tests import(create_admin, create_admin2, create_attendant, create_product, empty_product, create_sale, \
login_admin, login_attendant, empty_login, empty_signup, empty_price, invalid_input, duplicate_product, edit_product)
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
        data=json.dumps(login_admin), content_type = 'application/json')
        message = json.loads(response.data.decode())
        return message["access_token"]

    def signup_user(self, create_attendant):
        self.signin_admin(login_admin)
        response = self.client.post('/api/v1/auth/signup', \
        data=json.dumps(create_attendant), content_type = 'application/json' , \
        headers={"Authorization":"Bearer "+ self.signin_admin(login_admin)})
        return response

    def signup_denied(self, create_attendant):
        self.signup_user(create_attendant)
        response = self.client.post('/api/v1/auth/signup', \
        data=json.dumps(create_attendant), content_type = 'application/json' , \
        headers={"Authorization":"Bearer "+ self.signin_attendant(login_attendant)})
        return response

    def signup_username(self, create_attendant):
        self.signup_user(create_attendant)
        response = self.client.post('/api/v1/auth/signup', \
        data=json.dumps(create_attendant), content_type = 'application/json' , \
        headers={"Authorization":"Bearer "+ self.signin_admin(login_admin)})
        return response

    def signin_attendant(self, login_attendant):
        self.signup_user(create_attendant)
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_attendant), content_type = 'application/json')
        token = json.loads(response.data.decode())
        return token["access_token"]

    def invalid_attendant_login(self, login_attendant):
        self.signup_user(create_attendant)
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_attendant), content_type = 'application/json')
        return response

    def add_a_product(self, create_product):        
        response = self.client.post("/api/v1/products", data=json.dumps(create_product), \
        headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)), \
        'content_type' : 'application/json'})
        return response  

    def admin_headers(self, create_product):        
       response = self.client.post("/api/v1/products", data=json.dumps(create_product), \
       headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
       'content_type' : 'application/json'})
       return response

    def attendant_headers(self, create_sale):        
       response = self.client.post("/api/v1/sales", data=json.dumps(create_sale), \
       headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)), \
       'content_type' : 'application/json'})
       return response

    def empty_product_name(self, empty_product):
        response = self.add_a_product(empty_product)
        return response

    def empty_price(self, empty_price):
        response = self.add_a_product(empty_price)
        return response
    
    def duplicate_product(self, duplicate_product):
        response = self.add_a_product(duplicate_product)
        return response

    def invalid_input(self, invalid_input):
        response = self.add_a_product(invalid_input)
        return response

    def get_products(self):
        response = self.client.get("/api/v1/products")
        return response

    def get_single_product(self):
        response = self.client.get("api/v1/products/1")
        return response

    def product_not_found(self):
        response = self.client.get("/api/v1/products/1000")
        return response

    def delete_product(self):
        response = self.client.delete("api/v1/products/1")
        return response

    def edit_a_product(self, edit_product):
        response = self.client.put("/api/v1/products/1", data=json.dumps(edit_product), \
        headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)),\
        'content_type' : 'application/json'}) 
        return response

    def edit_product_denied(self, edit_product):
        response = self.client.put("/api/v1/products/1", data=json.dumps(edit_product), \
        headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response       

    def admin_name(self, create_admin2):
        response = self.register_admin(create_admin2)
        return response

    def home_route(self):
        response = self.client.get("/")
        return response

    def add_a_sale(self, create_sale):
        response = self.client.post("/api/v1/sales", data=json.dumps(create_sale), \
        headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response
    
    def get_sales_denied(self):
        response = self.client.get("/api/v1/sales", headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response

    def empty_sale_name(self, empty_sale):
        response = self.client.post("/api/v1/sales", data=json.dumps(empty_sale), \
        headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response

    def invalid_sale_price(self, invalid_sale_price):
        response = self.client.post("/api/v1/sales", data=json.dumps(invalid_sale_price), \
        headers={'Authorization':'Bearer '+ str(self.signin_attendant(login_attendant)), \
        'content_type' : 'application/json'})
        return response

    def get_sales(self):
        response = self.client.get("/api/v1/sales", headers={'Authorization':'Bearer '+ str(self.signin_admin(login_admin)), \
        'content_type' : 'application/json'})
        return response

    def get_a_sale(self):
        response = self.client.get("/api/v1/sales/1")
        return response

    def sale_not_found(self):
        response = self.client.get("/api/v1/sales/1000")
        return response
