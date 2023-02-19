import unittest

from library_project.customers.customer import Customer

class CustomerTestCase(unittest.TestCase):
    def test_set_email(self):
        customer = Customer("206661225", "Gal Mesilati", "Herzeliya", "gmsy@gmail.com", "28/03/2000")
        customer.set_customer_email("gal@gmail.com")
        new_email = customer.get_customer_email()
        self.assertEqual("gal@gmail.com", new_email, 'should be the same email')

    def test_set_address(self):
        customer = Customer("206661225", "Gal Mesilati", "Herzeliya", "gmsy@gmail.com", "28/03/2000")
        customer.set_customer_address("Tel Aviv")
        new_address = customer.get_customer_address()
        self.assertEqual("Tel Aviv", new_address, 'should be the same address')


if __name__ == '__main__':
    unittest.main()

