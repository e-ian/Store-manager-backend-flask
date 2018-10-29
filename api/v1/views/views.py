"""
module views
"""
from flask import Flask, jsonify, request, make_response
from api.v1.validators import Validate
from api.v1.models import Datastore
from api.v1.db_actions import Products

product= Products()

app=Flask(__name__)
# post_product = product.add_product()
# print (post_product)

@app.route('/')
def index():
    """default home route"""
    return jsonify({'message': 'welcome to store manager'})

@app.route('/api/v1/products', methods=['POST'])
def post_product():
    """ implements the post products api  """
    try:
        
        form_data = request.get_json(force=True)
        product = {
            'product_name': form_data['product_name'],
            'category' : form_data['category'],
            'price' : form_data['price'],
            'quantity' : form_data['quantity'],
            'minimum_quantity' : form_data['minimum_quantity']
        }
        valid = Validate(product['product_name'], product['category'], product['price'], \
        product['quantity'], product['minimum_quantity']).validate_product_post_input()
        # pro = Products()
        if valid is True:
            # product_add = pro.add_product(product)
            if product_add:
                return make_response(jsonify({"message": 'product added successfully'}), 201)
        return valid
    except Exception:
        return jsonify({'error': "Invalid input format"}), 400

