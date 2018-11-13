from tests.base import TestUser
from . import create_admin, create_attendant, create_product, create_sale, login_admin, login_attendant


class TestApp(TestUser):

    def test_add_product(self):
        response = self.add_a_product(create_product)
        self.assertIn("product added successfully", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_add_sale(self):
        response = self.add_a_sale(create_sale)
        self.assertIn("sale order added successfully", str(response.data))
        self.assertEqual(response.status_code, 201)
