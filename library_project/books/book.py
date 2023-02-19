import datetime

from library_project.utils.functions import validate_year, get_id_from_file, validate_loan_type


class Book:
    def __init__(self, name: str, author: str, year_published: str, type_loan, book_id=None):
        if book_id is None:
            self._book_id = get_id_from_file("book")
        else:
            self._book_id = book_id
        self._name = name
        self._author = author
        if validate_year(year_published) is True:
            self._year_published = int(year_published)
        if validate_loan_type(type_loan) is True:
            self._type_loan = int(type_loan)

    def get_book_id(self):
        return self._book_id

    def get_book_name(self):
        return self._name

    def set_book_name(self, change_name: str):
        self._name = change_name

    def get_book_author(self):
        return self._author

    def set_book_author(self, change_author: str):
        self._author = change_author

    def get_book_year_published(self):
        return self._year_published

    def set_year_published(self, change_year_published: int):
        if validate_year(change_year_published) is True:
            self._year_published = change_year_published

    def get_book_type_loan(self):
        return self._type_loan
