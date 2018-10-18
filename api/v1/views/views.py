"""
module
"""

from api.v1 import app
from flask import jsonify, request, make_response
from api.v1.models.products import Products

product_store = Products()


@app.route('/api/v1/products', methods=['POST'])
def post_product():
    """
    post products    
    """

    form_data = request.get_json(force=True)
    product_name = form_data['product_name']
    category = form_data['category']
    price = form_data['price']
    quantity = form_data['quantity']
    minimum_quantity = form_data['minimum_quantity']
    add = product_store.add_product(product_name, category, price, quantity, minimum_quantity)

    if add:
        message = {
            'message': 'Product successfully added'
        }

        return make_response(jsonify(message), 201)
    else:
        return make_response(jsonify(dict(message= 'Not added.')), 401)
