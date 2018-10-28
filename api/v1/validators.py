from flask import Flask, jsonify
class Validate:
    def __init__(self, *args):
        self.product_name = args[0]
        self.category = args[1]
        self.price = args[2]
        self.quantity = args[3]
        self.minimum_quantity = args[4]

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

    def validate_sale_order(self):
        """method to validate sale order inputs"""
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
        return True
       