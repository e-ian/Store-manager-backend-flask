"""
module views
"""
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api.v1 import app
from api.v1.validators import Validate
from api.v1.db_actions import Products, Sales, Users
from api.v1.models import Datastore

a = Products()
b = Sales()
c = Users()
validator = Validate()

@app.route('/')
def index():
    """default home route"""
    return jsonify({'message': 'welcome to store manager'})

@app.route('/api/v1/products', methods=['POST'])
@jwt_required
def post_product():
    """ implements the post products api  """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return make_response(jsonify({'message': "Unauthorised access"}), 401)
    try:        
        form_data = request.get_json(force=True)
        product_item = {
                'product_name': form_data['product_name'],            
                'price' : form_data['price'],
                'category' : form_data['category'],
                'quantity' : form_data['quantity'],
                'minimum_quantity' : form_data['minimum_quantity']
            }
        if not Validate.validate_prod_name_and_category(product_item['product_name'], \
        product_item['category']):
            return make_response(jsonify({"Message": "Product_name or category cannot be empty and takes alphabets"}), 400)
        elif not Validate.validate_price_and_quantity(product_item['price'], \
        product_item['quantity'], product_item['minimum_quantity']):
            return make_response(jsonify({"message": 'Price, quantity and minimum_quantity fields cannot be empty and should be an integer '}), 400)
        
        check_product = a.check_product(product_item['product_name'])
        if check_product:
            return make_response(jsonify({"message": "product already exists"}), 400)
        else:
            a.add_product(product_item)
            return make_response(jsonify({"message": 'product added successfully'}), 201)
    except Exception:
        return make_response(jsonify({"error": 'invalid input format'}), 400)
        
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
@jwt_required
def edit_product(product_id):
    """method to edit or modify an existing product"""
    try:
        current_user = get_jwt_identity()
        if current_user['role'] != 'admin':
            return make_response(jsonify({'message': "Unauthorised access"}), 401)    
        pdt_list = a.get_single_product(product_id)
        data = request.get_json(force=True)
        if pdt_list:
            a.modify_product(data['product_id'], data['product_name'], data['price'], \
            data['category'], data['quantity'], data['minimum_quantity'])
            return make_response(jsonify({'message': 'product edited'}), 200)
        else:
            return make_response(jsonify({'message': 'product does not exist'}), 404)
    except Exception:
        return make_response(jsonify({"error": 'invalid input format'}), 400)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """method to delete a product"""
    pdt_list = a.get_single_product(product_id)
    if pdt_list:
        a.delete_product(product_id)
        return make_response(jsonify({'message': 'product deleted'}), 200)
    else:
        return make_response(jsonify({'message': 'product doesnot exist'}), 404)

@app.route('/api/v1/sales', methods=['POST'])
@jwt_required
def post_sale_order():
    """ adds a sale order """
    current_user = get_jwt_identity()
    if current_user['role'] != 'attendant':
        return make_response(jsonify({'message': "Unauthorised access"}), 401)
    try:
        data = request.get_json(force=True)
        sale_order = {
            "product_name": data['product_name'],
            "price": data["price"],
            "quantity": data["quantity"]
        }
        if not Validate.validate_prod_name(sale_order['product_name']):
            return make_response(jsonify({"Message": "Product_name cannot be empty and takes alphabets"}), 400)
        elif not Validate.validate_sale_price_and_quantity(sale_order['price'], \
        sale_order['quantity']):
            return make_response(jsonify({"message": 'Price and quantity fields cannot be empty and should be an integer '}), 400)
        else:
            exist_product = a.check_product(sale_order['product_name'])
            if exist_product:
                b.add_sale_order(sale_order)
                return make_response(jsonify({"message": 'sale order added successfully'}), 201)
            else:
                return make_response(jsonify({"message": 'Product not in inventory'}), 404)
    except Exception:
        return make_response(jsonify({"error": 'invalid input format'}), 400)

@app.route('/api/v1/sales')
@jwt_required
def get_all_sale_orders():
    """implements get all sale orders endpoint"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return make_response(jsonify({'message': "Unauthorised access"}), 401)

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

@app.route('/api/v1/auth/signup', methods=['POST'])
@jwt_required
def user_register():
    """method implementing the register user endpoint"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return make_response(jsonify({'message': "Unauthorised access"}), 401)   
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']
    valid_username = validator.validate_input_str(username)
    valid_role = validator.validate_input_str(role)
    valid_password = validator.validate_password(password) 
    if valid_username:
        return valid_username   
    if valid_role:
        return valid_role
    check_user = c.check_username(username)  
    if check_user:
        return make_response(jsonify({"message": "username already exits"}), 400)
    if valid_password:
        return valid_password
    register_data = {
        "username": username,
        "password": password,
        "role": role
    }
    c.register_user(register_data)
    return make_response (jsonify({"message": 'User registered successfully'}), 201)

@app.route('/api/v1/auth/admin', methods=['POST'])
def register_admin():
    """method implementing register admin endpoint"""
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']

    valid_name = validator.validate_input_str(username)
    valid_role = validator.validate_input_str(role)
    valid_pass = validator.validate_password(password)
    if valid_name:
        return valid_name
    if valid_role:
        return valid_role
    check_name = c.check_username(username)
    if check_name:
        return make_response(jsonify({"message": "username already taken"}), 400)
    if valid_pass:
        return valid_pass
    admin_data = {
        "username": username,
        "password": password,
        "role": role
    }
    c.add_admin(admin_data)
    return make_response (jsonify({"message": 'Admin successfully registered'}), 201)

@app.route('/api/v1/auth/login', methods=['POST'])
def log_a_user():
    """method implementing api for logging in user"""
    login_data ={
        "username": request.json["username"],
        "password": request.json["password"]
    }
    user_login = c.login_users(login_data)    
    if not user_login:
        return make_response(jsonify({"message":"Username does not exist"}), 404)
    pass_check = c.check_password(user_login["password"], login_data["password"])
        
    if user_login and pass_check:
        access_token = create_access_token(identity=user_login)
        return make_response(jsonify({"access_token":access_token}), 200)
    else:
        return make_response(jsonify({"message": "username or password is wrong"}), 400)