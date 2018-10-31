from flask import Flask, jsonify
class Validate:

    @staticmethod
    def validate_prod_name_and_category(product_name, category):
        """method to validate product_name and category inputs"""
        if not product_name or not category or product_name.isspace() or category.isspace() \
        or not isinstance(product_name, str) or not isinstance(category, str):
            return False
        else:
            return True
    @staticmethod
    def validate_price_and_quantity(price, quantity, minimum_quantity):
        """method to validate price, quantity and minimum quantity inputs"""
        if not price or not quantity or not minimum_quantity or not isinstance(price, int) \
        or not isinstance(quantity, int) or not isinstance(minimum_quantity, int):
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
