"""
module test
"""
from api.v1 import app
from api.v1.views import views
import unittest
import json
from config import TestingConfig
from api.v1.models.products import Products




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
                    
  