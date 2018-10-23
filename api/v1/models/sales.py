"""
defines sales class in models
"""
from flask import Flask, jsonify, make_response, request
class Sales:
    sale_orders = []

    def __init__(self, product_name, price, quantity):
        """initializes Sales"""
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    # def to_json_format(self):
    #     """
    #     returns data in json format
    #     """
    #     return self.__dict__
    @classmethod
    def len_of_orders(cls):
        return len(cls.sale_orders) + 1

    @classmethod
    def add_sale_order(cls, sale):
        """
        class method to add a sale order to sale_order
        """
        cls.sale_orders.append(sale)
        return cls.sale_orders

    @classmethod
    def fetch_sale_orders(cls):
        return cls.sale_orders

    @classmethod
    def fetch_specific_sale_record(cls, sale_id):
        for sale_order in cls.sale_orders:
            if sale_order['sale_id'] == sale_id:
                return sale_order

    def validate_sale_order(self):
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
    