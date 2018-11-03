from Books import *
from Users import *

class TomeRater(object):
    def __init__(self):
        self.users = {}   # email : User object
        self.books = {}   # Book object: # users that read it

    def create_book(self, title, isbn):
        new_book = Books(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1  # indicates book has been read by user
            else:
                self.books[book] = 1   # indicates book has been read by first user
        else:
            print("No user with email {}!".format(email))
        return

    def add_user(self, name, email, user_books=None):
        self.users[email] = Users(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        read_count = 0
        for book in self.books:
            if self.books[book] >= read_count:
                read_count = self.books[book]
                most_read_book = book
        return most_read_book.title

    def highest_rated_book(self):
        high_rating = 0
        for book in self.books:
            book_rating = book.get_average_rating()
            if book_rating >= high_rating:
                high_rating = book_rating
                highest_rated_book = book
        return highest_rated_book.title

    def most_positive_user(self):
        positive_rating = 0
        for email in self.users:
            user = self.users.get(email)
            user_rating = user.get_average_rating()
            if user_rating >= positive_rating:
                positive_rating = user_rating
                most_positive_user = email
        return self.users[most_positive_user]

