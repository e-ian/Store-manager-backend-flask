"""
module products class in models
"""

from flask import Flask, jsonify, make_response, request
class Products():
    product_list = []

    def __init__(self, product_name, category, price, quantity, minimum_quantity):
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.minimum_quantity = minimum_quantity

    def json_format(self):
        """
        returns data in json format
        """
        return self.__dict__
    @classmethod
    def len_of_dict(cls):
         return len(cls.product_list) + 1

    @classmethod
    def add_product(cls, product):
        """
        class method to add a product to product_list
        """
        cls.product_list.append(product)
        return cls.product_list
    @classmethod
    def get_products(cls):        
        return cls.product_list
    
    @classmethod
    def get_single_product(cls, product_id):
        for product in cls.product_list:
            if product['product_id'] == product_id:
                return product

    
    