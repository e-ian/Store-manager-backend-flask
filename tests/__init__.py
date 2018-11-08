from config import Testingconfig
from api.v1 import app

create_admin = {
    "username": "ogwal",
    "password": "qwerty",
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

create_sale = {
    "product_name": "shoe",
    "price" : 30000, "quantity": 1
}

login_admin = {
    "username": "ogwal",
    "password": "qwerty"
}
login_attendant = {"username": "emma", "password": "qwerty123"}
