from library_project.customers.customer import Customer
from library_project.file_hendler import add_object_to_file, fetch_all, write_all
from ..Library.library import library
from pprint import pprint
from ..exceptions.exceptions import CustomerNotExist, NoEnteredCustomerId, InvalidCustomerID
from ..utils.functions import validate_name


def add_new_customer():
    customer_id = input("Please enter the national id: ")
    full_name = input("Please enter the customer's full name with a capital letter in the first and last name: ")
    address = input("Please enter a address by city with capital letter in first:")
    email = input("Please enter email:")
    birthdate = input("Please enter birthdate in format dd/mm/yyyy:")

    customer = Customer(customer_id, full_name, address, email, birthdate)
    add_object_to_file(customer, 'customer')
    print("Customer added successfully")
    return


def display_all_customers():
    pprint(fetch_all('customers'))


def remove_customer_from_the_library():
    customer_id = input('Please enter customer personal id: ')
    if customer_id == '':
        raise NoEnteredCustomerId(customer_id)
    try:
        customer_id = int(customer_id)
    except:
        raise InvalidCustomerID(customer_id)
    customers = library.get_customers()
    for customer in customers:
        if int(customer['id']) == customer_id:
            customers.remove(customer)
            write_all('customers', customers)
            print("delete customer successfully")
            return
    raise CustomerNotExist(customer_id)


def find_customer_by_name():
    customer_full_name = input("Enter the name of the customer: ")
    if validate_name(customer_full_name) is True:
        customers = fetch_all('customers')
        for customer in customers:
            if customer["full_name"] == customer_full_name:
                pprint(customer)
                return customer
        raise CustomerNotExist(customer_full_name)


