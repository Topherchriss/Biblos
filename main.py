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
        self.button_display_borrowed_books = tk.Button(master, text="Borrowed Books", command=self.display_borrowed_books)
        self.button_display_available_books = tk.Button(master, text="Available Books", command=self.display_available_books)

        # arrange labels and entry widgets in a grid layout
        self.label_user_id.grid(row=0, column=0, sticky=tk.E)
        self.entry_user_id.grid(row=0, column=1)

        self.label_first_name.grid(row=1, column=0, sticky=tk.E)
        self.entry_first_name.grid(row=1, column=1)

        self.label_last_name.grid(row=2, column=0, sticky=tk.E)
        self.entry_last_name.grid(row=2, column=1)

        self.label_email.grid(row=3, column=0, sticky=tk.E)
        self.entry_email.grid(row=3, column=1)

        self.label_book_id.grid(row=0, column=2, sticky=tk.E)
        self.entry_book_id.grid(row=0, column=3)

        self.label_title.grid(row=1, column=2, sticky=tk.E)
        self.entry_title.grid(row=1, column=3)

        self.label_author.grid(row=2, column=2, sticky=tk.E)
        self.entry_author.grid(row=2, column=3)

        self.label_ISBN.grid(row=3, column=2, sticky=tk.E)
        self.entry_ISBN.grid(row=3, column=3)


        # create buttons
        self.button_borrow.grid(row=5, column=0, columnspan=1)
        self.button_return.grid(row=5, column=2, columnspan=1)
        self.button_display_borrowed_books.grid(row=6, column=0, columnspan=1)
        self.button_display_available_books.grid(row=6, column=2, columnspan=1)

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


    #Define methods to borrow or return a book
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
                    messagebox.showerror("Error", f"User ID {user.user_id} has already borrowed {book.title} by {book.author}")
                else:
                    user.borrow_book(book)
                    messagebox.showinfo("Borrow Book", f"{user.first_name} has succefully borrowed {book.title} by {book.author}")
                    #Clear the entry fields
                    self.entry_user_id.delete(0, 'end')
                    self.entry_book_id.delete(0, 'end')
            else:
                messagebox.showerror("Error", f"{book.title} by {book.author} is not available for borrowing")
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
                messagebox.showinfo("Return Book", f" {book.title} by {book.author} returned by {user.first_name} user ID: {user.user_id}")
            else:
                messagebox.showerror("Error",f"{user.first_name}, User ID {user.user_id}, has not borrowed {book.title} therefore cannot return it")

                #Clear entry fields
                self.entry_user_id.delete(0, 'end')
                self.entry_book_id.delete(0, 'end')
        else:
            messagebox.showerror("Error", "User ID or Book ID not found")


    #Method for displaying borrowed books
    def display_borrowed_books(self):
        user_id = self.entry_user_id.get()
        user = self.find_user_by_id(user_id)

        if user is not None:
            borrowed_books = [book.title for book in user.books_borrowed]
            if borrowed_books:
                messagebox.showinfo("Your Borrowed Books", f"{user.first_name} {user.last_name}'s Borrowed Books:\n{' '.join(borrowed_books)}")
            else:
                messagebox.showinfo("Borrowed Books", f"{user.first_name} {user.last_name} has not borrowed any book. ")
        else:
            messagebox.showerror("Error", f"User ID is not valid")


    #Method for displaying available books
    def display_available_books(self):
        available_books = [book.title for book in self.library.book_inventory if book.availability]
        messagebox.showinfo("Available Books", f"Available books in the libray: \n{', '.join(available_books)}")



#Creating User class instance
user1 = User("77282", "Yale","Nalanze", "yalenalanze@gmail.com")
user2 = User("77255", "Mopao", "silikoti", "silikoti@gmail.com")
user3 = User("76754", "Kiki", "Mokonzi", "mokonzi@gmail.com")
user4 = User("77256", "Jeje", "Mukeba", "mukeba@gmail.com")

#creating instance for Book class
book1 = Book("100", "Python Essentials", "Python software foundation", "978-0-316-76948-0", True)
book2 = Book("101", "Hello Earth", "Marsians", "978-0-316-76948-0", True)
book3 = Book("102", "Karibu Kenya", "Mkenya Halisi", "978-0-316-76948-0", True)
book4 = Book("103", "Stop air polution", "Concerned Humans", "978-0-316-76948-0", True)
book5 = Book("104", "Data Science Fundamentals", "Data Science Community", "978-1-234-56789-0", True)
book6 = Book("105", "Introduction to Machine Learning", "ML Experts", "978-2-345-67890-1", True)
book7 = Book("106", "History of the Universe", "Cosmic Researchers", "978-3-456-78901-2", True)
book8 = Book("107", "Artificial Intelligence Explained", "AI Wizards", "978-4-567-89012-3", True)

library = Library()

#register users and add books to library
library.register_user(user1)
library.register_user(user2)
library.register_user(user3)
library.register_user(user4)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)


# Creating the Tkinter window
root = tk.Tk()

# Creating the LibraryGUI instance
library_gui = LibraryGUI(root, library)

# Running the Tkinter event loop
root.mainloop()