from flask import Flask, jsonify
import re
class Validate:
    def __init__(self, *args):
        self.product_name = args[0]
        self.category = args[1]
        self.price = args[2]
        self.quantity = args[3]
        self.minimum_quantity = args[4]

    def validate_prod_name_and_category(self):
        """method to validate product_name and category inputs"""
        if not self.product_name or not self.category or self.product_name.isspace() or self.category.isspace() \
        or not isinstance(self.product_name, str) or not isinstance(self.category, str):
            return False
        else:
            return True

    def validate_price_and_quantity(self):
        """method to validate price, quantity and minimum quantity inputs"""
        if self.price or not self.quantity or not self.minimum_quantity or not isinstance(self.price, int) \
         or not isinstance(self.quantity, int) or not isinstance(self.minimum_quantity, int):
            return False
        else:
            return True

    @staticmethod
    def validate_prod_name(product_name):
        """method to validate product name input of a sale order"""
        if not product_name or product_name.isspace() or not isinstance(product_name, str):
            return False
        else:
            return True

    @staticmethod
    def validate_sale_price_and_quantity(price, quantity):
        """method to validate price and quantity inputs of sale order"""
        if not price or not quantity or not isinstance(price, int) or not isinstance(quantity, int):
            return False
        else:
            return True

    @staticmethod
    def validate_input_str(input_str):
        """method to validate if input is string"""
        if re.search(r'\s', input_str):
            return jsonify({'error': "input field cannot have empty spaces"}), 400
        if re.search(r'\d', input_str):
            return jsonify({'error': "input field shouldnot have digits but letters"}), 400
        if re.search(r'\W', input_str):
            return jsonify({'error': "input field should have alphabets only"}), 400

    @staticmethod
    def validate_password(password):
        """method to validate password input"""
        if not len(password) >= 6:
            return jsonify({"error": "password length should be equal or greater than 6"}), 400
        if not re.search(r'\d', password):
            return jsonify({"error": "password should contain a digit"}), 400
        if not re.search(r'\W', password):
            return jsonify({"error": "password should contain some alpha numeric characters"}), 400
        


   