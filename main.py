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