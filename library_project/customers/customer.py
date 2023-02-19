import datetime
from library_project.utils.functions import get_id_from_file, validate_email, validate_name, validate_birth_date, validate_customer_id, validate_address_by_city

class Customer:
    def __init__(self,customer_id: str, full_name: str, address: str, email: str, birth_date: str, suspended_until=None):
        if validate_customer_id(customer_id) is True:
            self._id = customer_id
        if validate_name(full_name) is True:
            self._full_name = full_name
        if validate_address_by_city(address) is True:
            self._address = address
        if validate_email(email) is True:
            self._email = email
        if validate_birth_date(birth_date) is True:
            self._birth_date = birth_date
        self._suspended_until = suspended_until

    def get_customer_id(self):
        return self._id

    def get_customer_full_name(self):
        return self._full_name

    def set_customer_full_name(self, new_name:str):
        if validate_name(new_name) is True:
            self._full_name = new_name

    def get_customer_address(self):
        return self._address

    def set_customer_address(self, new_address: str):
        self._address = new_address

    def get_customer_email(self):
        return self._email

    def set_customer_email(self, new_email):
        if validate_email(new_email) is True:
            self._email = new_email

    def get_customer_birth_date(self):
        return self._birth_date

    def get_suspended_until(self):
        return self._suspended_until

    def set_suspended_until(self, late_date):
        self._suspended_until = late_date


