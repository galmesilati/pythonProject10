import datetime

from library_project.menus.book_menu import add_new_book, display_all_books, find_books_by_name, find_books_by_author, remove_book_from_the_library
from library_project.menus.customer_menu import add_new_customer, display_all_customers, remove_customer_from_the_library, find_customer_by_name
from library_project.menus.loan_menu import add_new_loan, display_all_loans, return_a_book, display_all_the_late_loans, display_past_loans_for_specifi_customer,display_current_loans_for_specifi_customer

main_menu = """
Welcome to the digital library
In the library app you can find a variety of reading books:
what do you want to do?
1  - add new customer
2  - add new book
3  - loan a book
    Each book in the library has a type of time for loan option.
     Type 1 - the book loan for 10 days,
     Type 2 - the book loan for 5 days,
     Type 3 - the book loan for 2 days
~ Please note ~ failure to return a book to the library on the correct date,
                will cause the customer to be suspended for two weeks.
                
4  - return a book
5  - display all books
6  - display all customers
7  - display all the loans
8  - display all the late loans
9  - display past loans for specific customer 
10 - display current loans for specific customer
11 - find books by name
12 - find books by author
13 - find customer by name
14 - remove a book from the library  
15 - remove a customer from the library 
16 - To exit a menu

"""

choices = range(1,17)


def menu():
    while True:
        try:
            print(main_menu)
            choice = int(input("enter your choice: "))
            if choice in choices:
                match choice:
                    case 1:
                        add_new_customer()
                    case 2:
                        add_new_book()
                    case 3:
                        add_new_loan()
                    case 4:
                        return_a_book()
                    case 5:
                        display_all_books()
                    case 6:
                        display_all_customers()
                    case 7:
                        display_all_loans()
                    case 8:
                        display_all_the_late_loans()
                    case 9:
                        display_past_loans_for_specifi_customer()
                    case 10:
                        display_current_loans_for_specifi_customer()
                    case 11:
                        find_books_by_name()
                    case 12:
                        find_books_by_author()
                    case 13:
                        find_customer_by_name()
                    case 14:
                        remove_book_from_the_library()
                    case 15:
                        remove_customer_from_the_library()
                    case 16:
                        print('bye bye')
                        exit()
        except Exception as e:
            print(f"Error: {e}, please try again ")







