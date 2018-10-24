"""
module views
"""

from api.v1 import app
from flask import jsonify, request, make_response
from api.v1.models.products import Products
from api.v1.models.sales import Sales

@app.route('/api/v1/products', methods=['POST'])
def post_product():
    """
    implements the post products api  
    """ 
    try:
        form_data = request.get_json(force=True)
        product = {
            'product_id': Products.len_of_dict(),
            'product_name': form_data['product_name'],
            'category' : form_data['category'],
            'price' : form_data['price'],
            'quantity' : form_data['quantity'],
            'minimum_quantity' : form_data['minimum_quantity']
        }
        valid=Products(product['product_name'], product['category'], product['price'], \
        product['quantity'], product['minimum_quantity']).validate_product_name_input()
        if valid==True:
            product_add = Products.add_product(product)
            if product_add:
                return make_response(jsonify({"message": 'product added successfully'}), 201)
        return valid  
    except KeyError:
        return jsonify({'error': "Invalid key fields"}), 400    

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
        return make_response(jsonify({'message': 'not found'}), 404)
    
@app.route('/api/v1/sales', methods=['POST'])
def post_sale_order():
    """
    adds a sale order
    """
    try:
        data = request.get_json(force=True)   
        sale_order={
            "sale_id": Sales.len_of_orders(),
            "product_name": data['product_name'],
            "price": data["price"],
            "quantity": data["quantity"]
        }    
        receipt = Sales(sale_order['product_name'], sale_order['price'], sale_order['quantity']).validate_sale_order()
        if receipt==True:
            create= Sales.add_sale_order(sale_order)
            if create:     
                return make_response(jsonify({'message': 'sale order added successfully'}), 201) 
        return receipt  
    except KeyError:
        return jsonify({'error': "missing one/ more key fields"}), 400       
    
@app.route('/api/v1/sales', methods=['GET'])
def get_sale_orders():
    """
    get all sale orders
    """
    if request.method == 'GET':
        all_sale_orders = Sales.fetch_sale_orders()
        response = {
            'sale_order_list':all_sale_orders
        }
        return make_response(jsonify(response), 200)

@app.route('/api/v1/sales/<int:sale_id>', methods=['GET'] )
def get_a_sale_order(sale_id):
    """
    get a specific sale order
    """
    get_sale_order = Sales.fetch_specific_sale_record(sale_id)

    if get_sale_order:
        message= {
            'sale':get_sale_order
            }
        return make_response(jsonify(message), 200)
    else:
        return make_response(jsonify({'message': 'not found'}), 404)
