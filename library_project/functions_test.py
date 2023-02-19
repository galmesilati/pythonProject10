import unittest

from library_project.books.book import Book
from library_project.exceptions.exceptions import BookTypeError, InvalidYear
from library_project.utils.functions import validate_loan_type, validate_year


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
        with self.assertRaises(InvalidYear):
            validate_year(2024)




if __name__ == '__main__':
    unittest.main()
