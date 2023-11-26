import tkinter as tk
from tkinter import messagebox


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


class LibraryGUI:
    def __init__ (self, master, library):
        self.master = master
        self.library = library
        self.master.title("Library Management System")

        #Labels for user information
        self.label_user_id = tk.Label(master, text="User ID:")
        self.label_first_name = tk.Label(master, text="First name:")
        self.label_last_name = tk.Label(master, text="Last name:")
        self.label_email = tk.Label(master, text="User email:")
        self.label_books_borrowed = tk.Label(master, text="Your borrowed books:")

        #Labels for Book Information
        self.label_book_id = tk.Label(master, text="Book ID:")
        self.label_title = tk.Label(master, text="Book Title: ")
        self.label_author = tk.Label(master, text="Book author:")
        self.label_ISBN = tk.Label(master, text="Book ISBN number:")
        self.label_availability = tk.Label(master, text="Book availability:")

        #create widgates for user info
        self.entry_user_id = tk.Entry(master)
        self.entry_first_name = tk.Entry(master)
        self.entry_last_name = tk.Entry(master)
        self.entry_email = tk.Entry(master)
        self.entry_books_borrowed = tk.Entry(master)

        #create widgates for book info
        self.entry_book_id = tk.Entry(master)
        self.entry_title = tk.Entry(master)
        self.entry_author = tk.Entry(master)
        self.entry_ISBN = tk.Entry(master)
        self.entry_availability = tk.Entry(master)

        #create buttons
        self.button_borrow = tk.Button(master, text="Borrow book", command=self.borrow_book)
        self.button_return =  tk.Button(master, text="Return borrowed book", command=self.return_book)

        # arrange labels and entry widgets in a grid layout
        self.label_user_id.grid(row=0, column=0, sticky=tk.E)
        self.entry_user_id.grid(row=0, column=1)

        self.label_first_name.grid(row=1, column=0, sticky=tk.E)
        self.entry_first_name.grid(row=1, column=1)

        self.label_last_name.grid(row=2, column=0, sticky=tk.E)
        self.entry_last_name.grid(row=2, column=1)

        self.label_email.grid(row=3, column=0, sticky=tk.E)
        self.entry_email.grid(row=3, column=1)

        self.label_books_borrowed.grid(row=4, column=0, sticky=tk.E)
        self.entry_books_borrowed.grid(row=4, column=1)

        self.label_book_id.grid(row=0, column=2, sticky=tk.E)
        self.entry_book_id.grid(row=0, column=3)

        self.label_title.grid(row=1, column=2, sticky=tk.E)
        self.entry_title.grid(row=1, column=3)

        self.label_author.grid(row=2, column=2, sticky=tk.E)
        self.entry_author.grid(row=2, column=3)

        self.label_ISBN.grid(row=3, column=2, sticky=tk.E)
        self.entry_ISBN.grid(row=3, column=3)

        self.label_availability.grid(row=4, column=2, sticky=tk.E)
        self.entry_availability.grid(row=4, column=3)

        # create buttons
        self.button_borrow.grid(row=5, column=0, columnspan=1)
        self.button_return.grid(row=5, column=2, columnspan=1)

    #Define methods to identify book and users by their ids
    def find_user_by_id(self, user_id):
        for user in self.library.users:
            if user.user_id == user_id:
                return user
        return None

    def find_book_by_id(self, book_id):
        for book in self.library.book_inventory:
            if book.book_id == book_id:
                return book
        return None



    def borrow_book(self):
        #get values from entry widgets
        user_id = self.entry_user_id.get()
        book_id = self.entry_book_id.get()

        # Find the user and book objects based on the entered IDs
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if user is not None and book is not None:
            if book.availability:
                if book in user.books_borrowed:
                    messagebox.showerror("Error", f"User ID {user.user_id} has already borrowed {book.title}")
                else:
                    user.borrow_book(book)
                    messagebox.showinfo("Borrow Book", f"Book {book.title} has been borrowed by user ID {user.user_id}")
                    #Clear the entry fields
                    self.entry_user_id.delete(0, 'end')
                    self.entry_book_id.delete(0, 'end')
            else:
                messagebox.showerror("Error", f"Book {book.title} is not available for borrowing")
        else:
            messagebox.showerror("Error", "User ID or book ID not found")

    def return_book(self):
        user_id = self.entry_user_id.get()
        book_id = self.entry_book_id.get()

        book = self.find_book_by_id(book_id)
        user = self.find_user_by_id(user_id)

        if user is not None and book is not None:
            if book in user.books_borrowed:
                user.return_book(book)
                messagebox.showinfo("Return Book", f"Book {book.title} returned by user ID: {user.user_id}")
            else:
                messagebox.showerror("Error",f"User ID {user.user_id} has not borrowed {book.title} therefore cannot return it")

                #Clear entry fields
                self.entry_user_id.delete(0, 'end')
                self.entry_book_id.delete(0, 'end')
        else:
            messagebox.showerror("Error", "User ID or Book ID not found")
