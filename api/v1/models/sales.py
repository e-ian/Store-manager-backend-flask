"""
defines sales class in models
"""
from flask import Flask, jsonify, make_response, request
class Sales():

    def __init__(self):
        """initializes sales_orders list"""
        self.sales_orders = []
    
    def add_sale_order(self, product_name, price, quantity):
        sales_dict = {}
        sales_dict['sale_id'] = len(self.sales_orders) + 1
        sales_dict['product_name'] = product_name
        sales_dict['price'] = price
        sales_dict['quantity'] = quantity       

        #appending to list of sale_orders

        self.sales_orders.append(sales_dict)
        message = {
            'message': 'sale order added successfully'
        }

        return make_response(jsonify(message), 201)

    def fetch_sale_orders(self):        
        return self.sales_orders

    def fetch_specific_sale_record(self, sale_id):
        for sale_order in self.sales_orders:
            if sale_order['sale_id'] == sale_id:
                return sale_order
