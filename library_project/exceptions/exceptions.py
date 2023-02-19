
class LibraryExceptions(Exception):
    """A base class for all library exceptions"""
    def __init__(self, element, massage):
        self.element = element
        self.massage = massage

    def __str__(self):
        return self.massage + str(self.element)


class CustomersErrors(LibraryExceptions):
    """A base class for all customers errors"""
    def __init__(self, customer_element, massage):
        self.element = customer_element
        self.massage = massage


class BooksErrors(LibraryExceptions):
    """A base class for all books errors"""
    def __init__(self, book_element, massage):
        self.element = book_element
        self.massage = massage


class LoansErrors(LibraryExceptions):
    """A base class for all loans errors"""
    def __init__(self, loan_element, massage):
        self.element = loan_element
        self.massage = massage


class InvalidCustomerID(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal ID"""
    def __init__(self, customer_id):
        massage = "This customer ID is not a legal: "
        super().__init__(customer_id, massage)


class InvalidCustomerName(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal name"""
    def __init__(self, customer_name):
        massage = "A customer's name should start with a capital letter in the first name and last name. you entered: "
        super().__init__(customer_name, massage)


class InvalidCustomerEmail(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal email"""
    def __init__(self, customer_email):
        massage = "Invalid email entered: "
        super().__init__(customer_email, massage)


class InvalidBirthDate(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal birthdate"""
    def __init__(self, customer_birthdate):
        massage = "The birthday date does not match the format dd/mm/yyyy : "
        super().__init__(customer_birthdate, massage)

class InvalidCustomerAddress(CustomersErrors):
    def __init__(self, city):
        massage = "The address entered is invalid. A valid address is a city name that begins with a capital letter. you entered: "
        super().__init__(city, massage)


class CustomerNotExist(CustomersErrors):
    def __init__(self, customer_name):
        massage = "Customer does not exist in the system: "
        super().__init__(customer_name, massage)


class InvalidDate(LoansErrors):
    """This exception will be raised if the user enters an invalid date"""
    def __init__(self, date):
        massage = "Date does not match the format dd/mm/yyyy : "
        super().__init__(date, massage)


class InvalidYear(BooksErrors):
    """This exception will raise if the user tries to add a book with an illegal publish year"""
    def __init__(self, year):
        massage = "They year must be positive integer with 4 digits, you entered "
        super().__init__(year, massage)


class TheBookSearchNotExisted(BooksErrors):
    """This exception will raise if the user enters an invalid value in the relevant search"""
    def __init__(self, search_by):
        massage = "The book does not exist in the system. with this name: "
        super().__init__(search_by, massage)


class BookUnavailable(BooksErrors):
    """This exception will raise if the user tries to reach a book id that does not exist in the database"""
    def __init__(self, book_id):
        massage = "This copy of book isn't available for loan "
        super().__init__(book_id, massage)


class BookDoesntExist(BooksErrors):
    """This exception will raise if the user tries to access a book that does not exist in the database"""
    def __init__(self, book_id):
        massage = "The book does not exist in the library: "
        super().__init__(book_id, massage)


class BookTypeError(BooksErrors):
    """This exception will raise if the user tries to add a book with a book type that is not 1, 2 or 3"""
    def __init__(self, book_type):
        massage = "The book type is incorrect. Correct book type is 1, 2 or 3. you entered: "
        super().__init__(book_type, massage)

class InvalidBookId(BooksErrors):
    def __init__(self, book_id):
        massage = "you did not insert a number: "
        super().__init__(book_id, massage)

class NoEnteredBookId(BooksErrors):
    def __init__(self, book_id):
        massage = "you did not insert a book id "
        super().__init__(book_id, massage)


class InvalidBookName(BooksErrors):
    def __init__(self, book_name):
        massage = "you did not insert a book name: "
        super().__init__(book_name, massage)

class InvalidAuthorName(BooksErrors):
    def __init__(self, author_name):
        massage = "you did not insert a author name: "
        super().__init__(author_name, massage)

class NoEnteredCustomerId(CustomersErrors):
    def __init__(self, customer_id):
        massage = "you did not insert a customer id"
        super().__init__(customer_id, massage)

