#from datetime import datetime
import datetime
from library_project.utils.functions import validate_date, get_id_from_file, validate_customer_id


class Loan:
    def __init__(self, customer_id: str, book_id, loan_date, loan_id=None, return_date=None):
        if loan_id is None:
            self._loan_id = get_id_from_file('loan')
        else:
            self._loan_id = loan_id
        if validate_customer_id(customer_id) is True:
            self._customer_id = customer_id
        self._book_id = book_id
        if validate_date(loan_date) is True:
            self._loan_date = loan_date
        self._return_date = return_date

    def get_loan_id(self):
        return self._loan_id

    def get_customer_id(self):
        return self._customer_id

    def get_book_id(self):
        return self._book_id

    def get_date_of_loan(self):
        return self._loan_date

    def get_return_date(self):
        return self._return_date



