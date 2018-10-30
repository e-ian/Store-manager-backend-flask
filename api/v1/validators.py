from flask import Flask, jsonify
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
        if not self.price or not self.quantity or not self.minimum_quantity or not isinstance(self.price, int) \
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
