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

        # query = "INSERT INTO products(product_name, category, price, \
        # quantity, minimum_quantity) VALUES('shoe', 'mens clothing', '3000', '1', '5')"
        # cursor.execute(query)
        # return True
