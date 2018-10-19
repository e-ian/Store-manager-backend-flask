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

        self.products =[{
            "product_name" : "jeans",
            "price" : 5000,
            "category":"mens clothing",
            "quantity": 10,
            "minimum_quantity": 5
            },
            {
            "product_name" : "shirts",
            "price" : 25000,
            "category":"mens clothing",
            "quantity": 12,
            "minimum_quantity": 4
        }]
        self.sales =[{
            "product_name" : "shoes",
            "price" : 25000,
            "quantity" : 100
            },
            {
            "product_name" : "suit",
            "price" : 250000,
            "quantity" : 1
            }]
    
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
            self.assertEqual(response.status_code, 201)
    
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
            self.assertEqual(response.status_code, 404)
    
    def test_post_sale_order(self):
        """
        tests if a sale order can be added
        """
        sale = {
            "product_name" : "shoes",
            "price" : 25000,
            "quantity" : 100
            }
        with self.client as client:
            response = client.post("/api/v1/sales", data= json.dumps(sale), content_type='application/json')
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
        tests if a specific sale order cannot be returned
        """
        with self.client as client:
            response = client.get("/api/v1/sales/1")
            self.assertEqual(response.status_code, 404)

    def teardown(self):
        self.sales.clear()
        self.products.clear()
    
  