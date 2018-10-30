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
        quantity='{}', minimum_quantity='{}' WHERE product_id='{}'".format(product_name, \
        price, category, quantity, minimum_quantity, product_id)
        dictcur.execute(query)
        return dictcur
        
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

    def register_user(self, data):
        """method to register a new user"""
        query = "INSERT INTO users(username, password, role) \
        VALUES('{}', '{}', 'user')".format(data['username'], \
        generate_password_hash(data['password']))
        cursor.execute(query)
        return data

