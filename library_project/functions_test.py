import unittest

from library_project.books.book import Book
from library_project.exceptions.exceptions import BookTypeError, InvalidYear, InvalidCustomerID, InvalidDate, \
    InvalidCustomerEmail, InvalidCustomerName
from library_project.utils.functions import validate_loan_type, validate_year, validate_customer_id, convert_to_date, \
    validate_date, validate_email, validate_name


class FunctionsTestCase(unittest.TestCase):
    def test_validate_loan_type(self):
        self.assertEqual(validate_loan_type(1), True, 'should be true')
        self.assertEqual(validate_loan_type(2), True, 'should be true')
        self.assertEqual(validate_loan_type(3), True, 'should be true')
        with self.assertRaises(BookTypeError):
            validate_loan_type(4)

    def test_validate_year(self):
        self.assertEqual(validate_year(2020), True, 'should be true')
        self.assertEqual(validate_year(2010), True, 'should be true')
        self.assertEqual(validate_year(2005), True, 'should be true')
        self.assertEqual(validate_year(2000), True, 'should be true')
        with self.assertRaises(InvalidYear):
            validate_year(2024)

    def test_validate_customer_id(self):
        self.assertEqual(validate_customer_id('206661225'), True, 'should be true')
        self.assertEqual(validate_customer_id('123456789'), True, 'should be true')
        with self.assertRaises(InvalidCustomerID):
            validate_customer_id('')

    def test_validate_date(self):
        self.assertEqual(validate_date('12/12/2000'),True, 'should be true')
        self.assertEqual(validate_date('12/10/1998'),True, 'should be true')
        self.assertEqual(validate_date('12/12/2020'),True, 'should be true')
        with self.assertRaises(InvalidDate):
            validate_date('12.12.2020')

    def test_validate_email(self):
        self.assertEqual(validate_email('gms@gmail.com'), True, 'should be true')
        self.assertEqual(validate_email('gms@outlook.co.il'), True, 'should be true')
        with self.assertRaises(InvalidCustomerEmail):
            validate_email('gmsylty@c')

    def test_validate_name(self):
        self.assertEqual(validate_name('Gal Mesilati'), True, 'should be true')
        self.assertEqual(validate_name('David Cohen'), True, 'should be true')
        self.assertEqual(validate_name('Chen Mesilati'), True, 'should be true')
        with self.assertRaises(InvalidCustomerName):
            validate_name('gal mesilati')

if __name__ == '__main__':
    unittest.main()
