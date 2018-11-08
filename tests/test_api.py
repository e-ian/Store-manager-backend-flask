from tests.base import TestUser
from tests.base import signup_user, signin_user, add_a_product

class TestApp(TestUser):

    def test_add_product(self):