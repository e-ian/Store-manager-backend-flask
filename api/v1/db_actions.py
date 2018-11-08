"""
module handling actions performed by the database
"""
from flask import make_response, jsonify, current_app as app
from api.v1.models import Datastore
from werkzeug.security import generate_password_hash, check_password_hash
db = Datastore()
cursor = db.cur
dictcur = db.dict_cursor

class Products:
    """class to handle operations on products"""

    def add_product(self, data):
        """method to add products"""        
        query = "INSERT INTO products(product_name, category, price, \
        quantity, minimum_quantity) VALUES('{}', '{}', '{}', '{}', '{}')".format(data['product_name'], \
        data['category'], data['price'], data['quantity'], data['minimum_quantity'])
        cursor.execute(query)
        return data

    def get_products(self):
        """method that returns all products"""
        query = "SELECT * FROM products"
        dictcur.execute(query)
        products = dictcur.fetchall()
        return products

    def get_single_product(self, product_id):
        """method that returns a single product"""
        query = "SELECT * FROM products WHERE product_id='{}'".format(product_id)
        dictcur.execute(query)
        single_product = dictcur.fetchone()
        return single_product

    def modify_product(self, product_id, product_name, price, category, quantity, minimum_quantity):
        """modifies or edits a single product"""
        query = "UPDATE products SET product_name='{}', price='{}', category='{}', \
        quantity='{}', minimum_quantity='{}' WHERE product_id='{}';".format(product_name, \
        price, category, quantity, minimum_quantity, product_id)
        dictcur.execute(query)
        return dictcur

    def delete_product(self, product_id):
        """method to delete a product"""
        query = "DELETE FROM products WHERE product_id='{}'".format(product_id)
        delete_prod = cursor.execute(query)
        return delete_prod       

    @staticmethod
    def check_product(product_name):
        """method to check if username exists"""
        query = "SELECT * FROM products WHERE product_name='{}'".format(product_name)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data
        
class Sales:
    """Class handling all operations on sales"""
    def add_sale_order(self, data):
        """method to add sale order"""
        query = "INSERT INTO sales(product_name, price, quantity) \
        VALUES('{}', '{}', '{}')".format(data['product_name'], data['price'], data['quantity'])

        cursor.execute(query)
        return data

    def get_sale_orders(self):
        """method to get all sale orders"""
        query = "SELECT * FROM sales"
        dictcur.execute(query)
        sales = dictcur.fetchall()
        return sales
    def get_specific_sale_order(self, sale_id):
        """method to get a specific sale order"""
        query = "SELECT * FROM sales WHERE sale_id='{}'".format(sale_id)
        dictcur.execute(query)
        specific_sale = dictcur.fetchone()
        return specific_sale

class Users:
    """Class handling all db actions on users"""

    def add_admin(self, data):
        """method to add an admin user"""
        query = "INSERT INTO users(username, password, role) VALUES(\
        '{}', '{}', 'admin')".format(data["username"], \
        generate_password_hash(data["password"]))
        cursor.execute(query)
        return_id = "SELECT user_id, username, role FROM users WHERE username = '{}'".format(data["username"])
        dictcur.execute(return_id)
        data = dictcur.fetchall()
        return data

    def register_user(self, data):
        """method to register a new user"""
        query = "INSERT INTO users(username, password, role) \
        VALUES('{}', '{}', '{}')".format(data['username'], \
        generate_password_hash(data['password']), data['role'])
        cursor.execute(query)
        return data

    def login_users(self, data):
        """method to login users"""
        query = "SELECT * FROM users WHERE username ='{}'".format(data['username'])
        dictcur.execute(query)
        login = dictcur.fetchone()
        return login
    
    @staticmethod
    def check_username(username):
        """method to check if username exists"""
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data

    def check_password(self, data, db_data):
        return check_password_hash(data, db_data)