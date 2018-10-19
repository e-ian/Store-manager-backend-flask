"""
module products class in models
"""

from flask import Flask, jsonify, make_response, request
class Products():

    def __init__(self):
        self.product_list = []

    def add_product(self, product_name, category, price, quantity, minimum_quantity):
        product_dict = {}
        product_dict['product_id'] = len(self.product_list) + 1
        product_dict['product_name'] = product_name
        product_dict['category'] = category
        product_dict['price'] = price
        product_dict['quantity'] = quantity
        product_dict['minimum_quantity'] = minimum_quantity

        #appending to list
        self.product_list.append(product_dict)
        message = {
            'message': 'Product successfully added'
        }

        return make_response(jsonify(message), 201)

    def get_products(self):        
        return self.product_list

    def get_single_product(self, product_id):
        for product in self.product_list:
            if product['product_id'] == product_id:
                return product

    
    