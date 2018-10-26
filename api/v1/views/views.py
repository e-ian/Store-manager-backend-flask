"""
module views
"""
from flask import jsonify, request, make_response
from api.v1 import app
from api.v1.models.products import Products
from api.v1.models.sales import Sales

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
            'product_id': Products.len_of_dict(),
            'product_name': form_data['product_name'],
            'category' : form_data['category'],
            'price' : form_data['price'],
            'quantity' : form_data['quantity'],
            'minimum_quantity' : form_data['minimum_quantity']
        }
        valid = Products(product['product_name'], product['category'], product['price'], \
        product['quantity'], product['minimum_quantity']).validate_product_post_input()
        if valid is True:
            product_add = Products.add_product(product)
            if product_add:
                return make_response(jsonify({"message": 'product added successfully'}), 201)
        return valid
    except Exception:
        return jsonify({'error': "Invalid input format"}), 400

@app.route('/api/v1/products')
def get_all_products():
    """  get all products    """
    all_products = Products.get_products()
    if all_products:
        return make_response(jsonify({'product_list':all_products}), 200)

@app.route('/api/v1/products/<int:product_id>')
def get_a_product(product_id):
    """ get a product by product_id """
    get_product = Products.get_single_product(product_id)
    if get_product:
        return make_response(jsonify({'product': get_product}), 200)
    else:
        return make_response(jsonify({'message': 'product not found'}), 404)

@app.route('/api/v1/sales', methods=['POST'])
def post_sale_order():
    """ adds a sale order """
    try:
        data = request.get_json(force=True)
        sale_order = {
            "sale_id": Sales.len_of_orders(),
            "product_name": data['product_name'],
            "price": data["price"],
            "quantity": data["quantity"]
        }
        receipt = Sales(sale_order['product_name'], sale_order['price'], \
        sale_order['quantity']).validate_sale_order()
        if receipt == True:
            create = Sales.add_sale_order(sale_order)
            if create:
                return make_response(jsonify({'message': 'sale order added successfully'}), 201)
        return receipt
    except KeyError:
        return jsonify({'error': "missing one or more key fields"}), 400

@app.route('/api/v1/sales')
def get_sale_orders():
    """ get all sale orders """
    all_sale_orders = Sales.fetch_sale_orders()
    if all_sale_orders:
        return make_response(jsonify({'sale_order_list': all_sale_orders}), 200)

@app.route('/api/v1/sales/<int:sale_id>')
def get_a_sale_order(sale_id):
    """ get a specific sale order """
    get_sale_order = Sales.fetch_specific_sale_record(sale_id)
    if get_sale_order:
        return make_response(jsonify({'sale':get_sale_order}), 200)
    else:
        return make_response(jsonify({'message': 'sale order not found'}), 404)
