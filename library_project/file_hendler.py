import json
from library_project.books.book import Book
from library_project.customers.customer import Customer
from library_project.loans.loan import Loan


#customers
def customer_to_customer_dict(customer) -> dict:
    return {
        "id" : customer.get_customer_id(),
        "full_name" : customer.get_customer_full_name(),
        "address" : customer.get_customer_address(),
        "email" : customer.get_customer_email(),
        "birthdate" : customer.get_customer_birth_date(),
        "suspended_until" : customer.get_suspended_until()
    }

#books
def book_to_book_dict(book) -> dict:
    return {
        "book_id" : book.get_book_id(),
        "book_name": book.get_book_name(),
        "author_name": book.get_book_author(),
        "book_year_published" : book.get_book_year_published(),
        "book_type_loan" : book.get_book_type_loan()
    }

#loans
def loan_to_loan_dict(loan) -> dict:
    return {
        "loan_id" : loan.get_loan_id(),
        "customer_id": loan.get_customer_id(),
        "book_id" : loan.get_book_id(),
        "loan_date" : loan.get_date_of_loan(),
        "return_date" : loan.get_return_date()
    }


def add_object_to_file(obj: Customer | Book | Loan, obj_type:str):
    file_path = ""
    object_dict = {}
    file_dict = []
    match obj_type:
        case 'customer':
            object_dict = customer_to_customer_dict(obj)
            file_path = "./customers/customers.json"
        case 'book':
            object_dict = book_to_book_dict(obj)
            file_path = "../library_project/books/books.json"
        case 'loan':
            object_dict = loan_to_loan_dict(obj)
            file_path = "../library_project/loans/loans.json"
    with open(file_path, "r") as f:
        file_dict = json.load(f)
    file_dict.append(object_dict)
    with open(file_path, "w") as f:
        json.dump(file_dict, f)


def fetch_all(display_type):
    file_path = ""
    match display_type:
        case 'customers':
            file_path = "./customers/customers.json"
        case 'books':
            file_path = "./books/books.json"
        case 'loans':
            file_path = "./loans/loans.json"
    with open(file_path, "r") as f:
        content = json.load(f)
        return content

def write_all(write_type, object_to_write):
    file_path = ""
    match write_type:
        case 'customers':
            file_path = "./customers/customers.json"
        case 'books':
            file_path = "./books/books.json"
        case 'loans':
            file_path = "./loans/loans.json"

    with open(file_path, 'w') as f:
        json.dump(object_to_write, f)


