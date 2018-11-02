"""
module test
"""
import unittest
import json
from api.v1.db_actions import Products
from api.v1.db_actions import Sales
from api.v1 import app
from api.v1.models import Datastore


class TestApi(unittest.TestCase):
    """ class for unittesting the APIs """
    def setUp(self):
        """ sets up instance of app for the tests
            creates client to run the tests
        """
        self.dstore = Datastore()
        self.client = app.test_client()

    def test_add_product(self):
        """tests if a product has been added"""
        product = {"product_name" : "socks",
                   "price" : 5000,
                   "category": "mens clothing",
                   "quantity": 10,
                   "minimum_quantity": 5}

        with self.client as client:
            res = client.post("api/v1/auth/login", data=json.dumps({"username":"ogwal", "password": "qwerty"}), \
            content_type='application/json')
            data = json.loads(res.data.decode())
            token = data['access_token']
            headers={"Authorization": "Bearer "+ token, "content_type" : "application/json"}
            response = client.post("/api/v1/products", data=json.dumps(product),\
            headers=headers)
            reply = json.loads(response.data.decode())
            self.assertEqual(reply['message'], "product added successfully")
            self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        """tests if all products can be fetched"""
        with self.client as client:
            response = client.get("/api/v1/products")
            self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        """tests if a single product can be fetched"""
        with self.client as client:
            response = client.get("/api/v1/products/1")
            self.assertEqual(response.status_code, 200)

    def test_product_not_found(self):
        """method to test if a product isnt returned by given product_id"""
        with self.client as client:
            client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=5))
            client.post("api/v1/products", json=dict(product_name="skirt", \
            price=5000, category="womens clothing", quantity=10, minimum_quantity=5))
            response = client.get("/api/v1/products/200")
            self.assertEqual(response.status_code, 404)

    def test_post_sale_order(self):
        """tests if a sale order can be added"""
        with self.client as client:
            res = client.post("api/v1/auth/login", data=json.dumps({"username":"emma", "password": "qwerty123"}), \
            content_type='application/json')
            data = json.loads(res.data)
            token = data['access_token']
            headers={"Authorization": "Bearer "+ token, "content_type" : "application/json"}
            response = client.post("/api/v1/sales", headers=headers, json=dict(product_name='jeans',\
            price=50000, quantity=3))
            self.assertEqual(response.status_code, 201)

    def test_get_sale_orders(self):
        """tests if all sales orders can be fetched"""
        with self.client as client:
            res = client.post("api/v1/auth/login", data=json.dumps({"username":"ogwal", "password": "qwerty"}), \
            content_type='application/json')
            data = json.loads(res.data)
            token = data['access_token']
            headers={"Authorization": "Bearer "+ token, "content_type" : "application/json"}
            response = client.get("/api/v1/sales", headers=headers)
            self.assertEqual(response.status_code, 200)

    def test_get_a_sale_order(self):
        """tests if a specific sale order can be returned"""
        with self.client as client:
            client.post("/api/v1/sales", json=dict(product_name='shoes', price=25000, quantity=10))
            client.post("/api/v1/sales", json=dict(product_name='suit', price=250000, quantity=1))
            response = client.get("/api/v1/sales/2")
            self.assertEqual(response.status_code, 200)

    def test_sale_order_not_found(self):
        """tests if a specific sale order cannot be found"""
        with self.client as client:
            client.post("/api/v1/sales", json=dict(product_name='jeans', price=50000, quantity=3))
            client.post("/api/v1/sales", json=dict(product_name='skirt', price=30000, quantity=10))
            response = client.get("/api/v1/sales/1000")
            self.assertEqual(response.status_code, 404)

            # tests to validate the inputs of a posted product
    def test_product_not_empty_string(self):
        """tests if product posted is not an empty string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name=" ", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)
    
    def test_category_not_empty_string(self):
        """tests if product posted is not an empty string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="jeans", \
            price=5000, category="    ", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_product_with_alphabet_only(self):
        """tests if product has alphabets only"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="123***", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_price_not_string(self):
        """tests if price is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price="5000", category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_price_is_integer(self):
        """tests if price is an integer"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=3.5, category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_quantity_not_string(self):
        """tests if quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity="ten", minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_quantity_is_integer(self):
        """tests if quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10.677, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_min_quantity_not_string(self):
        """tests if minimum_quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity="five"))
            self.assertEqual(response.status_code, 400)

    def test_min_quantity_integer(self):
        """tests if minimum quantity is an integer"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=6.8))
            self.assertEqual(response.status_code, 400)

    def test_key_error_post_product(self):
        """tests for keyError when a key is missing"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, quantity=10, minimum_quantity=6))
            self.assertEqual(response.status_code, 400)

            #validating sale order inputs
    def test_product_name_not_empty_string(self):
        """tests if product_name posted is not an empty string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name=" ", \
            price=5000, quantity=10))
            self.assertEqual(response.status_code, 400)

    def test_product_name_with_alphabet_only(self):
        """tests if product_name has alphabets only"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="123***", \
            price=5000, quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_price_not_string(self):
        """tests if sale price is not a string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price="5000", quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_price_is_integer(self):
        """tests if sale price is an integer"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=3.5, quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_quantity_not_string(self):
        """tests if quantity sold is not a string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=5000, quantity="ten"))
            self.assertEqual(response.status_code, 400)

    def test_sale_quantity_is_integer(self):
        """tests if quantity sold is an integer"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=5000, quantity=10.677))
            self.assertEqual(response.status_code, 400)

    def test_invalid_key_post_sale(self):
        """tests for invalid key when a key is missing"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(price=5000, quantity=10))
            self.assertEqual(response.status_code, 400)



    def test_home_route(self):
        """test for the default home route"""
        with self.client as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 
