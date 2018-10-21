"""
module
"""

from api.v1 import app
from flask import jsonify, request, make_response
from api.v1.models.products import Products
from api.v1.models.sales import Sales


sales_store = Sales()

@app.route('/api/v1/products', methods=['POST'])
def post_product():
    """
    post products    
    """

    form_data = request.get_json(force=True)
    product = {
        'product_id': Products.len_of_dict(),
        'product_name': form_data['product_name'],
        'category' : form_data['category'],
        'price' : form_data['price'],
        'quantity' : form_data['quantity'],
        'minimum_quantity' : form_data['minimum_quantity']
    }  
   
    product_add = Products.add_product(product)
    if product_add:
        message = {
            'message': 'Product successfully added'
        }

        return make_response(jsonify(message), 201)
    else:
        return make_response(jsonify(dict(message= 'No product added')), 400)

@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """
    get all products
    """
    if request.method == 'GET':
        all_products = Products.get_products()
        response = {
            'product_list':all_products
        }
        return make_response(jsonify(response), 200)

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_a_product(product_id):
    """
    get a product by product_id
    """    
    get_product = Products.get_single_product(product_id)
    if get_product:
        response = {
            'product':get_product
        }
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify({'response': 'not found'}), 404)

    """
    handling sales orders
    """

@app.route('/api/v1/sales', methods=['POST'])
def post_sale_order():
    """
    adds a sale order
    """
    data = request.get_json(force=True)
    product_name = data['product_name']
    price = data['price']
    quantity = data['quantity']
    create= sales_store.add_sale_order(product_name, price, quantity)

    if create:
        message = {
            'message': 'sale order added successfully'
        }
        return make_response(jsonify(message), 201)
    else:
        return make_response(jsonify({'message': "No sale order added"}), 400)
    
@app.route('/api/v1/sales', methods=['GET'])
def get_sale_orders():
    """
    get all sale orders
    """
    if request.method == 'GET':
        all_sale_orders = sales_store.fetch_sale_orders()
        response = {
            'sale_order_list':all_sale_orders
        }
        return make_response(jsonify(response), 200)

@app.route('/api/v1/sales/<int:sale_id>', methods=['GET'] )
def get_a_sale_order(sale_id):
    """
    get a specific sale order
    """
    get_sale_order = sales_store.fetch_specific_sale_record(sale_id)

    if get_sale_order:
        message= {
            'sale':get_sale_order
            }
        return make_response(jsonify(message), 200)

    else:
        return make_response(jsonify({'message': 'not found'}), 404)
