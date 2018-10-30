"""
module views
"""
from flask import Flask, jsonify, request, make_response
from api.v1 import app
from api.v1.validators import Validate
from api.v1.models import Datastore
from api.v1.db_actions import Products
from api.v1.db_actions import Sales, Users

a = Products()
b = Sales()
c = Users()

@app.route('/')
def index():
    """default home route"""
    return jsonify({'message': 'welcome to store manager'})

@app.route('/api/v1/products', methods=['POST'])
def post_product():
    """ implements the post products api  """
        
    form_data = request.get_json(force=True)
    product_item = {
            'product_name': form_data['product_name'],            
            'price' : form_data['price'],
            'category' : form_data['category'],
            'quantity' : form_data['quantity'],
            'minimum_quantity' : form_data['minimum_quantity']
        }
    valid = Validate(product_item['product_name'], product_item['category'], product_item['price'], \
        product_item['quantity'], product_item['minimum_quantity'])
    if not valid.validate_prod_name_and_category():
        return make_response(jsonify({"Message": "Product_name or category cannot be empty and takes alphabets"}), 400)
    elif not valid.validate_price_and_quantity():
        return make_response(jsonify({"message": 'Price, quantity and minimum_quantity fields cannot be empty and should be an integer '}), 400)
    else:
        a.add_product(product_item)
        return make_response(jsonify({"message": 'product added successfully'}), 201)

@app.route('/api/v1/products')
def get_all_products():
    """implements get all products api"""
    all_products = a.get_products()
    if all_products:
        return make_response(jsonify({'product_list':all_products}), 200)

@app.route('/api/v1/products/<int:product_id>')
def get_a_product(product_id):
    """ method to get a product by product_id """
    get_product = a.get_single_product(product_id)
    if get_product:
        return make_response(jsonify({'product': get_product}), 200)
    else:
        return make_response(jsonify({'message': 'product not found'}), 404)

@app.route('/api/v1/products/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    """method to edit or modify an existing product"""
    pdt_list = a.get_single_product(product_id)
    data = request.get_json(force=True)
    if pdt_list:
        a.modify_product(data['product_id'], data['product_name'], data['price'], data['category'], data['quantity'], data['minimum_quantity'])
        return make_response(jsonify({'message': 'product edited'}),200)
    else:
        return make_response(jsonify({'message': 'product doesnot exist'}), 404)

@app.route('/api/v1/sales', methods=['POST'])
def post_sale_order():
    """ adds a sale order """
    data = request.get_json(force=True)
    sale_order = {
        "product_name": data['product_name'],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    if not Validate.validate_prod_name(sale_order['product_name']):
        return make_response(jsonify({"Message": "Product_name cannot be empty and takes alphabets"}), 400)
    elif not Validate.validate_sale_price_and_quantity(sale_order['price'], sale_order['quantity']):
        return make_response(jsonify({"message": 'Price and quantity fields cannot be empty and should be an integer '}), 400)
    else:
        b.add_sale_order(sale_order)
        return make_response(jsonify({"message": 'sale order added successfully'}), 201)

@app.route('/api/v1/sales')
def get_all_sale_orders():
    """implements get all sale orders endpoint"""
    sale_orders = b.get_sale_orders()
    if sale_orders:
        return make_response(jsonify({'sale_list': sale_orders}), 200)

@app.route('/api/v1/sales/<int:sale_id>')
def get_a_sale_order(sale_id):
    """method to get a one sale order"""
    get_sale = b.get_specific_sale_order(sale_id)
    if get_sale:
        return make_response(jsonify({"sale order": get_sale}), 200)
    else:
        return make_response(jsonify({"message": 'sale order not found'}), 404)

@app.route('/api/v1/auth/login', methods=['POST'])
def log_a_user():
    """meyth"""
    login_data ={
        "username": request.json['username'],
        "password": request.json['password']
    }

    user_login = c.login_users(login_data)
    if not user_login:
        return make_response(jsonify({"message": 'user not found'}), 404)
    pass_check = c.check_password(login_data, user_login)
    if pass_check:
        return make_response(jsonify({"message": 'login successful'}), 200)

