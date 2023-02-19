from .. import file_hendler
from ..utils.functions import validate_customer_id
from ..exceptions.exceptions import CustomerNotExist, BookDoesntExist

class Library:
    def __init__(self):
        self._customers = []
        self._books = []
        self._loans = []

    def get_customers(self):
        if len(self._customers) == 0:
            self._customers = file_hendler.fetch_all('customers')
        return self._customers

    def get_books(self):
        if len(self._books) == 0:
            self._books = file_hendler.fetch_all('books')
        return self._books

    def get_loans(self):
        if len(self._loans) == 0:
            self._loans = file_hendler.fetch_all('loans')
        return self._loans

    def get_book_by_book_id(self, book_id):
        books = self.get_books()
        for book in books:
            if int(book["book_id"]) == int(book_id):
                return book
        raise BookDoesntExist(book_id)

    def get_customer_by_customer_id(self, customer_id):
        if validate_customer_id(customer_id) is True:
            customers = self.get_customers()
            for customer in customers:
                if customer['id'] == customer_id:
                    return customer
            raise CustomerNotExist(customer_id)


library = Library()
