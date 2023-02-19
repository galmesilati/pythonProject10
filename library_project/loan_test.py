import datetime
import unittest

from library_project.Library.library import library
from library_project.books.book import Book
from library_project.customers.customer import Customer
from library_project.file_hendler import add_object_to_file, write_all
from library_project.loans.loan import Loan
from library_project.utils.functions import validate_return_loan
from library_project.menus.customer_menu import remove_customer_from_the_library

class LoanTestCase(unittest.TestCase):
    def test_add_a_new_loan_and_return(self):
        """
        This test is a unit-test that tests all the flow of the system
        it tests: creation of user, creation of book, make a loan, return a loan, delete a customer, delete a book.
and     also write and read to json files.
        """
        result = None
        book = Book('Harry potter', "harry", '1990', '2')
        customer = Customer('206661225', 'Gal Mesilati', 'Herzeliya', 'gms@gmail.com', '28/03/2000')
        loan = Loan('206661225', book.get_book_id(), datetime.date.today().strftime('%d/%m/%Y'))
        add_object_to_file(customer, 'customer')
        add_object_to_file(book, 'book')
        add_object_to_file(loan, 'loan')
        customer_id = '206661225'
        customer = library.get_customer_by_customer_id(customer_id)
        book_id = book.get_book_id()
        loans = library.get_loans()
        del loan
        for loan in loans:
            if int(loan["book_id"]) == book_id:
                book = library.get_book_by_book_id(book_id)
                loan_type = book["book_type_loan"]
                today = datetime.date.today()
                return_date = today.strftime('%d/%m/%Y')
                if validate_return_loan(return_date,loan['loan_date'], loan_type) is True:
                    loan["return_date"] = return_date
                    write_all('loans', loans)
                    result = True
        customer_id = 206661225
        customers = library.get_customers()
        for customer in customers:
            if int(customer['id']) == customer_id:
                customers.remove(customer)
                write_all('customers', customers)
        books = library.get_books()
        for book in books:
            if int(book['book_id']) == book_id:
                books.remove(book)
                write_all('books', books)
        self.assertEqual(result, True, 'should be the same')



if __name__ == '__main__':
    unittest.main()
