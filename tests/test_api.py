from tests.base import TestUser
from . import (create_admin, create_admin2, create_attendant, create_product, create_sale, create_sale2, login_admin, \
login_attendant, empty_product, empty_price, duplicate_product, invalid_input, edit_product, invalid_sale, empty_sale, \
invalid_sale_price, invalid_username, invalid_username2, empty_role, short_password, invalid_password, admin_role, \
invalid_attendant, admin_pass, invalid_userpass)

class TestApp(TestUser):

    def test_add_product(self):
        response = self.add_a_product(create_product)
        self.assertIn("product added successfully", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_admin_headers(self):
        response = self.admin_headers(create_product)
        self.assertIn("Unauthorised access", str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_empty_product(self):
        response = self.empty_product_name(empty_product)
        self.assertIn("Product_name or category cannot be empty and takes alphabets", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_price(self):
        response = self.empty_price(empty_price)
        self.assertIn("Price, quantity and minimum_quantity fields cannot be empty and should be an integer", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_duplication(self):
        self.add_a_product(create_product)
        response = self.duplicate_product(duplicate_product)
        self.assertIn("product already exists", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_input(self):
        response = self.invalid_input(invalid_input)
        self.assertIn("invalid input format", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_get_products(self):
        self.add_a_product(create_product)
        response = self.get_products()
        self.assertEqual(response.status_code, 200)

    def test_single_product(self):
        self.add_a_product(create_product)
        response = self.get_single_product()
        self.assertEqual(response.status_code, 200)

    def test_product_not_found(self):
        self.add_a_product(create_product)
        response = self.product_not_found()
        self.assertIn("product not found", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        self.add_a_product(create_product)
        self.get_single_product()
        response = self.delete_product()
        self.assertIn("product deleted", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_deleted_product(self):
        self.get_single_product()
        response = self.delete_product()
        self.assertIn("product doesnot exist", str(response.data))
        self.assertEqual(response.status_code, 404)
    
    def test_edit_product(self):
        self.add_a_product(create_product)
        self.get_single_product()
        response = self.edit_a_product(edit_product)
        self.assertIn("product edited", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_denied(self):
        self.test_edit_product()
        response = self.edit_product_denied(edit_product)
        self.assertIn("Unauthorised access", str(response.data))
        self.assertEqual(response.status_code, 401)
        
    def test_invalid_edit(self):
        self.add_a_product(create_product)
        self.get_single_product()
        response = self.edit_a_product(create_product)
        self.assertIn("invalid input format", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_missing_product(self):
        response = self.edit_a_product(edit_product)
        self.assertIn("product does not exist", str(response.data))
        self.assertEqual(response.status_code, 404)      

    def test_home_route(self):
        response = self.home_route()
        self.assertIn("welcome to store manager", str(response.data))

    def test_add_sale(self):
        self.add_a_product(create_product)
        response = self.add_a_sale(create_sale)
        self.assertIn("sale order added successfully", str(response.data))
        self.assertEqual(response.status_code, 201)
    
    def test_attendant_headers(self):
        self.test_add_sale()
        response = self.attendant_headers(create_sale)
        self.assertIn("Unauthorised access", str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_invalid_sale(self):
        self.test_add_sale()
        response = self.add_a_sale(invalid_sale)
        self.assertIn("invalid input format", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_sale(self):
        response = self.empty_sale_name(empty_sale)
        self.assertIn("Product_name cannot be empty and takes alphabets", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_sale_price(self):
        response = self.invalid_sale_price(invalid_sale_price)
        self.assertIn("Price and quantity fields cannot be empty and should be an integer", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_non_existent_product(self):
        self.test_add_sale()
        response = self.add_a_sale(create_sale2)
        self.assertIn("Product not in inventory", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_get_sales_denied(self):
        self.test_add_sale()
        response = self.get_sales_denied()
        self.assertIn("Unauthorised access", str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_get_sales(self):
        self.test_add_sale()
        response = self.get_sales()
        self.assertEqual(response.status_code, 200)

    def test_get_a_sale(self):
        self.test_get_sales()
        response = self.get_a_sale()
        self.assertEqual(response.status_code, 200)
    
    def test_sale_not_found(self):
        self.test_get_sales()
        response = self.sale_not_found()
        self.assertIn("sale order not found", str(response.data))
        self.assertEqual(response.status_code, 404)
        
    def test_register_admin(self):
        response = self.register_admin(create_admin)
        self.assertIn("Admin successfully registered", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_admin_name(self):
        self.register_admin(create_admin)
        response = self.admin_name(create_admin)
        self.assertIn("username already taken", str(response.data))
        self.assertEqual(response.status_code, 400)
        response = self.admin_name(create_admin2)
        self.assertIn("input field should have alphabets only", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_admin_role(self):
        self.register_admin(create_admin)
        response = self.admin_name(admin_role)
        self.assertIn("input field cannot have empty spaces", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_admin_password(self):
        self.register_admin(create_admin)
        response = self.admin_name(admin_pass)
        self.assertIn("password should contain alphanumeric characters", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_signup_user(self):
        self.test_register_admin()
        response = self.signup_user(create_attendant)
        self.assertIn("User registered successfully", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_signup_denied(self):
        self.test_signup_user()
        response = self.signup_denied(create_attendant)
        self.assertIn("Unauthorised access", str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_signup_username(self):
        self.test_signup_user()
        response = self.signup_username(create_attendant)
        self.assertIn("username already exits", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_username(self):
        self.test_signup_user()
        response = self.signup_user(invalid_username)
        self.assertIn("input field should have alphabets only", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_username2(self):
        self.test_signup_user()
        response = self.signup_user(invalid_username2)
        self.assertIn("input field shouldnot have digits but letters", str(response.data))
        self.assertEqual(response.status_code, 400)
        response = self.signup_user(empty_role)
        self.assertIn("input field cannot have empty spaces", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_password(self):
        self.test_signup_user()
        response = self.signup_user(short_password)
        self.assertIn("password length should be equal or greater than 6", str(response.data))
        self.assertEqual(response.status_code, 400)
        response = self.signup_user(invalid_password)
        self.assertIn("password should contain alphanumeric characters", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        self.signup_user(create_attendant)
        response = self.invalid_attendant_login(invalid_attendant)
        self.assertIn("Username does not exist", str(response.data))
        self.assertEqual(response.status_code, 404)
        response = self.invalid_attendant_login(invalid_userpass)
        self.assertIn("username or password is wrong", str(response.data))
        self.assertEqual(response.status_code, 400)
        