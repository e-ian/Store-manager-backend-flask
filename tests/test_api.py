"""
module test
"""
from api.v1 import app
from api.v1.views import views
import unittest
import json
from config import TestingConfig
from api.v1.models.products import Products
from api.v1.models.sales import Sales




class TestApi(unittest.TestCase):
    """
    class for unittesting the apis
    """
    def setUp(self):
        """
        sets up instance of app for the tests
        creates client to run the tests
        """
        # self.app = create_app(TestingConfig)
        self.client = app.test_client()
    
    def test_add_product(self):
        """
        tests if a product has been added, test asserts that response is 201
        """
        product = {"product_name" : "jeans",
            "price" : 5000,
            "category":"mens clothing",
            "quantity": 10,
            "minimum_quantity": 5}

        
        with self.client as client:
            response = client.post("/api/v1/products", data = json.dumps(product), content_type='application/json')
            
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('Product successfully added', response_json['message'])
    
    # def test_product_empty(self):
    #     """
    #     method to test if post method returns invalid if no product is entered
        
    #     """
    #     product = {"product_name" : "",
    #         "price": "",
    #         "category": "",
    #         "quantity": "",
    #         "minimum_quantity": ""}
            
    #     with self.client as client:
    #         response = client.post('/api/v1/products', data = json.dumps(product), content_type='application/json')
    #         self.assertEqual(response.status_code, 400)
            

    
    def test_get_products(self):
        """
        tests if all products can be fetched
        test asserts that response is 200
        """       
        with self.client as client:
            response = client.get("/api/v1/products")
            self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        """
         tests if a single product cannot be fetched
        """
        
        with self.client as client:                     
            response = client.get("/api/v1/products/1")             
            self.assertEqual(response.status_code, 200)
    
    def test_product_not_found(self):
        """
        method to test if a product isnt returned by given product_id
        """
        with self.client as client:
            client.post("api/v1/products", json=dict(product_name= "vest", price='5000', category="mens clothing", quantity= '10',minimum_quantity='5'))
            client.post("api/v1/products", json=dict(product_name= "skirt", price='5000', category="womens clothing", quantity= '10',minimum_quantity='5'))
            response = client.get("/api/v1/products/20")
            self.assertEqual(response.status_code, 404)
    
    def test_post_sale_order(self):
        """
        tests if a sale order can be added
        """
        with self.client as client:
            response = client.post("/api/v1/sales", json=dict(product_name='jeans', price='50000', quantity='3' ))            
            self.assertEqual(response.status_code, 201)
    
    def test_get_sale_orders(self):
        """
        tests if all sales orders can be fetched
        """
        with self.client as client:
            response = client.get("/api/v1/sales")
            self.assertEqual(response.status_code, 200)

    def test_get_a_sale_order(self):
        """
        tests if a specific sale order can be returned
        """
        with self.client as client:
            client.post("/api/v1/sales", json=dict(product_name='shoes', price='25000', quantity='10' ))
            client.post("/api/v1/sales", json=dict(product_name='suit', price='250000', quantity='1' ))
            response = client.get("/api/v1/sales/2")
            self.assertEqual(response.status_code, 200)

    def test_sale_order_not_found(self):
        """
        tests if a specific sale order cannot be found
        """
        with self.client as client:
            client.post("/api/v1/sales", json=dict(product_name='jeans', price='50000', quantity='3' ))
            client.post("/api/v1/sales", json=dict(product_name='skirt', price='30000', quantity='10' ))
            response = client.get("api/v1/sales/10")
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


    
  