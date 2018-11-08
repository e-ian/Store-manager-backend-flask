from tests.base import TestUser
from . import create_admin, create_attendant, create_product, create_sale, login_admin, login_attendant


class TestApp(TestUser):

    def test_add_product(self):
        self.add_a_product(create_product)
        self.register_admin(create_admin)
        self.signin_admin(login_admin)
        response = self.add_a_product(create_product)
        self.assertEqual(response.status_code, 201)
