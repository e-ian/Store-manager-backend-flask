from tests import(create_admin, create_attendant, create_product, create_sale, login_admin)
from tests.base import TestUser

class TestApi(TestUser):

    def test_post_product(self):
        self.signup_user(create_admin)
        self.signin_user(login_admin)
        response = self.add_a_product(create_product)
        self.assertEqual(response.status_code, 201)
