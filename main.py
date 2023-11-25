class User:
    def __init__(self, user_id, first_name, last_name, email):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            self.books_borrowed.append(book)
            print(f"{self.first_name} {self.last_name} (ID {self.user_id}) has succefully borrowed {book.title}")

        else:
            print(f"Dear {self.first_name} {self.last_name} {book.title} is not available for checkout")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.availability = True
            self.books_borrowed.remove(book)
            print(f"{book.title} borrowed by {self.first_name} {self.last_name} has succefully been returned. Thank you for your coperation")
        else:
            print(f"Dear {self.first_name} {self.last_name} {book.title} is not in your list of borrowed books!")

    def __str__(self):
        return f"ID: {self.user_id} Name: {self.first_name} {self.last_name} Email: {self.email} Books borrowed: {self.books_borrowed}"


class Book:
    def __init__(self, book_id, title, author, ISBN, availability = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    def check_out(self, user):
        if self.availability:
            self.availability = False
            user.books_borrowed.append(self)
            print(f"{user.first_name} {user.last_name} (ID: {user.user_id}) has succefully check_out {book_title}")
        else:
            print(f"{self.book_title} is not available for check-out!")

    def return_book(self, user):
        if self in user.books_borrowed:
            self.availability = True
            user.books_borrowed.remove(self)
            print(f"{user.first_name} {user.last_name} (ID: {user.user_id}) has succefully returned {self.title}")
        else:
            print(f"{self.title} is not in your borrowed books!")

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Availability: {self.availability}"



class Library:
    def __init__(self):
        self.book_inventory = []
        self.users = []

    def add_book(self, book):
        self.book_inventory.append(book)

    def remove_book(self, book):
        self.book_inventory.remove(book)

    def register_user(self, user):
        self.users.append(user)

    def unregister_user(self, user):
        self.users.remove(user)

    def __str__(self):
        book_list = [str(book) for book in self.book_inventory]
        user_list = [str(user) for user in self.users]
        return f"State of library: \nBooks:\n{'\n'.join(book_list)}\nUsers:\n{'\n'.join(user_list)}"