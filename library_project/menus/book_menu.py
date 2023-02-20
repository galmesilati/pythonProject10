import json
from pprint import pprint

from library_project.books.book import Book
from library_project.file_hendler import add_object_to_file, fetch_all, write_all
from .loan_menu import is_book_available
from ..Library.library import library
from ..exceptions.exceptions import TheBookSearchNotExisted, InvalidBookName, InvalidAuthorName, InvalidBookId, NoEnteredBookId

# This function is a creation of book and also write to json files.
def add_new_book():
    book_name = input("enter the name of book: ")
    author_name = input("Please enter the author's name: ")
    book_year_published = input("Please enter the year of book was published")
    book_type_loan = input("Please enter the book type for loan time")

    book = Book(book_name, author_name,book_year_published, book_type_loan)
    add_object_to_file(book, 'book')
    print("Book added successfully")
    return


def display_all_books():
    pprint(fetch_all('books'))


# This function searches for a book by book name and returns the book.
def find_books_by_name():
    book_name = input("Enter the name of the book: ")
    if book_name == "":
        raise NoEnteredBookId(book_name)
    books = fetch_all('books')
    for book in books:
        if book["book_name"] == book_name:
            pprint(book)
            return book
    raise TheBookSearchNotExisted(book_name)


# This function searches for a book by author name and returns the book
def find_books_by_author():
    author_name = input("Enter the name of the author of the book: ")
    if author_name == "":
        raise InvalidAuthorName(author_name)
    books = fetch_all('books')
    for book in books:
        if book["author_name"] == author_name:
            pprint(book)
            return book
    raise TheBookSearchNotExisted(author_name)


# This function deletes a book from the system only if the book is available and not loaned.
def remove_book_from_the_library():
    book_id = input('Please enter book id: ')
    if book_id == '':
        raise NoEnteredBookId(book_id)
    try:
        book_id = int(book_id)
    except:
        raise InvalidBookId(book_id)
    books = library.get_books()
    if is_book_available(book_id) == True:
        for book in books:
            if int(book['book_id']) == book_id:
                books.remove(book)
                write_all('books', books)
                print("Delete book successfully")
                return
            print("The book does not exist to remove it")




