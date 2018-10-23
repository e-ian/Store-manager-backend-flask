"""
module products class in models
"""

from flask import Flask, jsonify, make_response, request

class Products:
    product_list = []

    def __init__(self, product_name, category, price, quantity, minimum_quantity):
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.minimum_quantity = minimum_quantity

    # def json_format(self):
    #     """
    #     returns data in json format
    #     """
    #     return self.__dict__
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
      
    def validate_post_input(self):
        if self.product_name.strip() == '':
            return jsonify({'error': "product name cannot be an empty string"}), 400 
        if not self.product_name.isalpha():
            return jsonify({'error': "product name should have alphabet letters only"}), 400         
        if isinstance(self.price, str):
            return jsonify({'error': "price cannot be a string"}), 400
        if not isinstance(self.price, int):
            return jsonify({'error': "input price as integer"}), 400
        if isinstance(self.quantity, str):
            return jsonify({'error': "quantity cannot be a string"}), 400
        if not isinstance(self.quantity, int):
            return jsonify({'error': "input quantity as integer"}), 400 
        if isinstance(self.minimum_quantity, str):
            return jsonify({'error': "minimum quantity cannot be a string"}), 400
        if not isinstance(self.minimum_quantity, int):
            return jsonify({'error': "input minimum quantity as integer"}), 400        
        if self.category.strip() == '':
            return jsonify({'error': "category cannot be an empty string"}), 400                   
        return True
    

    
    