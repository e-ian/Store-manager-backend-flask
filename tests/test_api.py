from tests.base import TestUser
from . import create_admin, create_attendant, create_product, create_sale, login_admin, login_attendant


class TestApp(TestUser):

    def test_add_product(self):
        response = self.add_a_product(create_product)
        self.assertIn("product added successfully", str(response.data))
        print(response)
        self.assertEqual(response.status_code, 201)
