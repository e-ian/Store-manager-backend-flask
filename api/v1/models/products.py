"""
module products class in models
"""

from flask import Flask, jsonify

class Products:
    """class for products model"""
    product_list = []

    def __init__(self, *args):
        self.product_name = args[0]
        self.category = args[1]
        self.price = args[2]
        self.quantity = args[3]
        self.minimum_quantity = args[4]

    @classmethod
    def len_of_dict(cls):
        """class method that returns length of product_list with increment"""
        return len(cls.product_list) + 1

    @classmethod
    def add_product(cls, product):
        """class method to add a product to product_list """
        cls.product_list.append(product)
        return cls.product_list

    @classmethod
    def get_products(cls):
        """class method to return all products"""
        return cls.product_list

    @classmethod
    def get_single_product(cls, product_id):
        """class method to return a single product"""
        for product in cls.product_list:
            if product['product_id'] == product_id:
                return product

    def validate_product_post_input(self):
        """method for validating inputs"""
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
    