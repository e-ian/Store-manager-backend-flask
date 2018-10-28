"""
module handling actions performed by the database
"""
from flask import make_response, jsonify, current_app as app
from api.v1.models import Datastore
from werkzeug.security import generate_password_hash, check_password_hash
db = Datastore()
cursor = db.cur
dictcur = db.dict_cursor

class Users:
    """class to handle db operations on users"""
    
    def register_user(self, data):
        """method to register a new user"""
        query = "INSERT INTO users(username, password, role) \
        VALUES('{}', '{}', 'user')".format(data['username'], \
        generate_password_hash(data['password']))
        cursor.execute(query)
        return data
    
    def log_user(self, username):
        """method to login a user"""
        login = ("SELECT * FROM users WHERE username='{}'"
        .format(username))
        dictcur.execute(login)
        user = dictcur.fetchall()
        return user

class Products:
    """class to handle operations on products"""

    def add_product(self, product_name, category, price, quantity, minimum_quantity ):
        """method to add products"""
        query = "INSERT INTO products(product_name, category, price, \
        quantity, minimum_quantity) VALUES('{}', '{}', '{}', '{}', '{}')".format(product_name, \
        category, price, quantity, minimum_quantity)
        cursor.execute(query)
        return product_name

    def get_products(self):
        """method that returns all products"""
        query = "SELECT * FROM products"
        dictcur.execute(query)
        data = dictcur.fetchall()
        return data

    def get_a_product(self, product_id):
        """method that returns a product by id"""
        query = "SELECT * FROM products WHERE product_id='{}'".format(product_id)
        dictcur.execute(query)
        single_product = dictcur.fetchone()
        return single_product

    def modify_product(self, product_id, product_name, category, price, quantity, minimum_quantity):
        """modifies or edits a single product"""
        query = "UPDATE products SET product_name='{}', category='{}', price='{}', \
        quantity='{}', minimum_quantity='{}' WHERE product_id='{}'".format(product_name, \
        category, price, quantity, minimum_quantity, product_id)
        dictcur.execute(query)
        data  = dictcur.fetchall()
        return data

    def delete_product(self, product_id, user_id):
        """method that deletes a product"""
        clear = ("DELETE from products WHERE product_id={} and user_id={}"\
        .format(product_id, user_id))
        cursor.execute(clear)
        return "Product deleted"
