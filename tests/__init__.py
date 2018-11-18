from config import Testingconfig
from api.v1 import app

create_admin = {
    "username": "ogwal",
    "password": "qwerty",
    "role": "admin"
}
create_admin2 = {
    "username": "*ian$#",
    "password": "qwerty",
    "role": "admin"
}
admin_role = {
    "username": "eian",
    "password": "qwerty",
    "role": " "
}
admin_pass = {
    "username": "eian",
    "password": "#$@@#%",
    "role": "admin"
}
create_attendant = {
    "username": "emma",
    "password": "qwerty123",
    "role": "attendant"
}
create_product = {
    "product_name": "jeans",
    "price" : 30000,
    "category":"mens clothing",
    "quantity": 1,
    "minimum_quantity": 2
}
edit_product = {
        "category": "mens clothing",
        "minimum_quantity": 2,
        "price": 10000,
        "product_id": 1,
        "product_name": "belt",
        "quantity": 20
}
duplicate_product = {
    "product_name": "jeans",
    "price" : 30000,
    "category":"mens clothing",
    "quantity": 1,
    "minimum_quantity": 2
}
invalid_input = {
    "price" : 30000,
    "category":"mens clothing",
    "quantity": 1,
    "minimum_quantity": 2
}
empty_product = {
    "product_name": " ",
    "price" : 30000,
    "category":"mens clothing45",
    "quantity": 1,
    "minimum_quantity": 2
}
empty_price = {
    "product_name": "jeans",
    "price" : "three",
    "category":"mens clothing",
    "quantity": " ",
    "minimum_quantity": 2
}
create_sale = {
    "product_name": "jeans",
    "price" : 30000, 
    "quantity": 1
}
create_sale2 = {
    "product_name": "basketball",
    "price" : 50000, 
    "quantity": 1
}
empty_sale = {
    "product_name": " ",
    "price" : 50000, 
    "quantity": 1
}
invalid_sale_price = {
    "product_name": "jeans",
    "price" : " ", 
    "quantity": "three"
}
invalid_sale = {
    "price" : 50000, 
    "quantity": 1
}
login_admin = {
    "username": "ogwal",
    "password": "qwerty"
}
login_attendant = {
    "username": "emma",
    "password": "qwerty123"
}
invalid_attendant = {
    "username": "alistair",
    "password": "qwerty123"
}
invalid_userpass = {
    "username": "emma",
    "password": "123456"
}
invalid_username = {
    "username" : "*gwal#",
    "password" : "qwerty123",
    "role" : "attendant"
}
invalid_username2 = {
    "username" : "007",
    "password" : "qwerty123",
    "role" : "attendant"
}
empty_role = {
    "username" : "ogwal",
    "password" : "qwerty123",
    "role" : " "
}
short_password = {
    "username" : "ian",
    "password" : "kla",
    "role" : "attendant"
}
invalid_password = {
    "username" : "ian",
    "password" : "@@###%&",
    "role" : "attendant"
}
empty_login = {
    "username" : " ",
    "password" : "qwerty123"
}
empty_signup = {
    "username": " ",
    "password": "12345",
    "role": "attendant"
}