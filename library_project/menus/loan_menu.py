import datetime
from pprint import pprint
from library_project.file_hendler import add_object_to_file, fetch_all, write_all
from library_project.loans.loan import Loan
from library_project.Library.library import library
from library_project.books.book import Book
from library_project.utils.functions import get_last_day_to_retuned,validate_return_loan
from ..exceptions.exceptions import BookDoesntExist, BookUnavailable, InvalidBookId, NoEnteredCustomerId, NoEnteredBookId, CustomerNotExist


def is_book_available(book_id):
    available = True
    for loan in library.get_loans():
        loan = Loan(loan["customer_id"], loan["book_id"], loan["loan_date"], loan["loan_id"], loan["return_date"])
        if book_id == int(loan.get_book_id()) and loan.get_return_date() is None:
            available = False
    return available


def add_new_loan():
    customer_id = input("Please enter customer national id: ")
    if customer_id == '':
        raise NoEnteredCustomerId(customer_id)
    book_id = input("Please enter a book id: ")
    if book_id == '':
        raise NoEnteredCustomerId(book_id)
    try:
        book_id = int(book_id)
    except:
        raise InvalidBookId(book_id)
    if is_book_available(book_id) is True:
        today = datetime.date.today()
        loan_date = today.strftime('%d/%m/%Y')
        loan = Loan(customer_id, book_id, loan_date)
        add_object_to_file(loan, 'loan')
        book = library.get_book_by_book_id(book_id)
        print("Find book: ", book)

        if book is not False:

            book = Book(book["book_name"], book['author_name'],book['book_year_published'], book['book_type_loan'])
            date = get_last_day_to_retuned(book.get_book_type_loan(),loan_date)
            return_date = date.strftime('%d/%m/%Y')
            print(f'the return date is: {return_date}')
            print("Loan successfully")
        else:
            raise BookDoesntExist(book_id)
    else:
       raise BookUnavailable(book_id)


def return_a_book():
    customer_id = input('Please enter your national id: ')
    if customer_id == '':
        raise NoEnteredCustomerId(customer_id)
    customer = library.get_customer_by_customer_id(customer_id)
    if customer is False:
        raise CustomerNotExist(customer_id)
    book_id = input('Please enter the book id number: ')
    if book_id == '':
        raise NoEnteredBookId(book_id)
    try:
        book_id = int(book_id)
    except:
        raise InvalidBookId(book_id)
    if is_book_available(book_id) is False:
        loans = library.get_loans()
        found_book = False
        return_on_time = False
        for loan in loans:
            if int(loan["book_id"]) == book_id:
                found_book = True
                book = library.get_book_by_book_id(book_id)
                loan_type = book["book_type_loan"]
                today = datetime.date.today()
                return_date = today.strftime('%d/%m/%Y')
                if validate_return_loan(return_date,loan['loan_date'], loan_type) is True:
                    return_on_time = True
                    loan["return_date"] = return_date
                    write_all('loans', loans)
                    print("Book retuned")
                    return
                else:
                    suspended = today + datetime.timedelta(days=14)
                    date_str = suspended.strftime('%d/%m%Y')
                    customer['suspended_until'] = date_str
                    return_on_time = False
                    loan["return_date"] = return_date
                    write_all('loans', loans)
                    print("Book retuned")
                    return
        if not found_book:
            print("The book is not loaned")
    else:
        print("The book cannot be return because is in the library")


def display_all_loans():
    pprint(fetch_all('loans'))


def display_past_loans_for_specifi_customer():
    customer_loans = []
    customer_id = input("Please enter customer national id:")
    if customer_id == "":
        raise NoEnteredCustomerId(customer_id)
    loans = library.get_loans()
    for loan in loans:
        if loan['customer_id'] == customer_id and loan['return_date'] is not None:
            customer_loans.append(loan)
    pprint(customer_loans)


def display_current_loans_for_specifi_customer():
    customer_loans = []
    customer_id = input("Please enter customer national id:")
    loans = library.get_loans()
    for loan in loans:
        if loan['customer_id'] == customer_id and loan['return_date'] is None:
            customer_loans.append(loan)
    pprint(customer_loans)


def display_all_the_late_loans():
    print("All the late loan: ")
    today = datetime.date.today()
    return_date = today.strftime('%d/%m/%Y')
    loans = library.get_loans()
    for loan in loans:
        if loan['return_date'] is None:
            book = library.get_book_by_book_id(loan['book_id'])
            loan_type = book["book_type_loan"]
            if validate_return_loan(return_date, loan['loan_date'],loan_type) is False:
                print(loan)






