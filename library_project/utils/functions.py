import re
from datetime import datetime, timedelta

from library_project.exceptions.exceptions import InvalidCustomerID, InvalidDate, InvalidCustomerEmail,InvalidBirthDate, InvalidCustomerName, InvalidCustomerAddress, InvalidYear, BookTypeError

# from library_project.exceptions.exceptions import

minimum_loan_type = 1
maximum_loan_type = 3

def validate_loan_type(loan_type):
    allowed_loan_types = range(minimum_loan_type, maximum_loan_type +1)
    if int(loan_type) in allowed_loan_types:
        return True
    else:
        raise BookTypeError(loan_type)


def validate_year(year):
    try:
        year = int(year)
        if year <= datetime.now().year and year >= -5000:
            return True
        else:
            raise InvalidYear(year)
    except:
        raise InvalidYear(year)


def validate_customer_id(customer_id:str):
    pattern = '^[0-9]{9}$'
    if re.search(pattern, customer_id):
        return True
    else:
        raise InvalidCustomerID(customer_id)


def get_id_from_file(id_type: str):
    current_id = None
    path = None
    match id_type:
        case "book":
            path = "C:\\Users\\gmsyl\\pythonProject10\\library_project\\books\\book_id.txt"
        case 'loan':
            path = 'C:\\Users\\gmsyl\\pythonProject10\\library_project\\loans\\loans_id.txt'
    with open(path, "r") as f:
        current_id = int(f.read())
    with open(path, "w") as f:
        f.write(str(current_id + 1))
    return current_id


def convert_to_date(date:str):
    try:
        format = '%d/%m/%Y'
        date_object = datetime.strptime(date, format)
        return date_object
    except:
        raise InvalidDate(date)


def validate_date(date: str):
    try:
        correct_date = convert_to_date(date)
        return True
    except:
        raise InvalidDate(date)


def validate_return_loan(retuned_date, loan_date, book_type:int):
    if validate_date(loan_date) and validate_date(retuned_date):
        if get_last_day_to_retuned(book_type,loan_date) >= convert_to_date(retuned_date):
            return True
        else:
            return False


def validate_email(email: str):
    pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if re.search(pattern,email):
        return True
    else:
        raise InvalidCustomerEmail(email)


def validate_birth_date(birthdate: str):
    format = "%d/%m/%Y"
    try:
        correct_birthdate = datetime.strptime(birthdate, format)
        return True
    except:
        raise InvalidBirthDate(birthdate)


def validate_name(name: str):
    # pattern = '^([A-Z][a-z]*)$'
    pattern = '^([A-Z][a-z]*) +([A-Z][a-z]*)$'
    if re.search(pattern, name):
        return True
    else:
        raise InvalidCustomerName(name)

def validate_address_by_city(city: str):
    pattern = '^([A-Z][a-z]+)$'
    if re.search(pattern, city):
        return True
    else:
        raise InvalidCustomerAddress(city)



def get_last_day_to_retuned(type_loan: int, loan_date):
    if validate_date(loan_date) is True and validate_loan_type(type_loan) is True:
        loan_date = convert_to_date(loan_date)
        days = 0
        if type_loan == 1:
            days = 10
        elif type_loan == 2:
            days = 5
        elif type_loan == 3:
            days = 2
        result = loan_date + timedelta(days=days)
        return result



if __name__ == '__main__':
    print(validate_address_by_city('Herzeliya'))
#     try:
#         validate_customer_id("hchc")
#     except CustomerExceptions as e:
#         print(f"Error: {e}")

    # print(validate_customer_id('023963l66'))
#     print(validate_year(1989))
#     print(1)
#     # print(get_id_from_file("book"))
#     print(validate_date("12/04/2022"))
#     print(2)
#     print(validate_birth_date("28/03/2000"))
#     print(3)
#     email = "galm@gmail.co.il"
#     print(validate_email(email))
#     print(get_last_day_to_retuned(1,'04/02/2023'))
#     print(5)
#     print(validate_loan_type(2))
#       print(validate_name('Gal Mesilati'))


