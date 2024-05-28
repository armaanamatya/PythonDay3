# Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library catalog system. 
# Create a Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for borrowing or not). 
# Create another Python class LibraryCatalog to manage the collection of books with following functionalities:
# Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects) get book details and get all books from the list of objects
# Lets say, we need a book borrowing process (what books are borrowed and what books are available for borrowing). 
# Implement logics to integrate this requirement in the above system. Design the classes with a clear focus on adhering to the Single Responsibility Principle(SRP) which represents that "A module should be responsible to one, and only one, actor."

# Implements state of a book
class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Available: {'Yes' if self.available else 'No'}"

# Implements the management of collection of books

class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def get_book_details(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return str(book)
        return "Book not found."

    def get_all_books(self):
        return [str(book) for book in self.books]

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    return f"You have successfully borrowed '{book.title}'"
                else:
                    return f"'{book.title}' is currently unavailable"
        return "Book not found."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.available = True
                return f"You have successfully returned '{book.title}'"
        return "Book not found."

book1 = Book("1984", "George Orwell", 1234567890, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 9876543210, "Classic")

library_catalog = LibraryCatalog()

library_catalog.add_book(book1)
library_catalog.add_book(book2)

for book in library_catalog.books:
    print(book)

print(library_catalog.borrow_book(1234567890))
print(library_catalog.borrow_book(9876543210))
print(library_catalog.borrow_book(1234567890))
print(library_catalog.return_book(9876543210))

# [Open-Closed Principle (OCP)] Download the python file from this link. Suppose we have a Product class that represents a generic product, 
# and we want to calculate the total price of a list of products. Initially, the Product class only has a price attribute, and we can calculate the total price of products based on their prices.
# Now, let's say we want to add a discount feature, where some products might have a discount applied to their prices. 
# To add this feature, we would need to modify the existing Product class and the calculate_total_price function, which violates the Open/Closed Principle. 
# Redesign this program to follow the Open-Closed Principle (OCP) which represents “Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

from abc import ABC

class Product(ABC):
    def __init__(self, price):
        self._price = price

    def get_price(self):
        pass

class RegularProduct(Product):
    def __init__(self, price):
        super().__init__(price)

    def get_price(self):
        return self._price

class DiscountedProduct(Product):
    def __init__(self, price, discount):
        super().__init__(price)
        self._discount = discount

    def get_price(self):
        return self._price * (1 - self._discount)

def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.get_price()
    return total_price

products = [RegularProduct(100), DiscountedProduct(50, 0.1), RegularProduct(75)]
print("Total Price:", calculate_total_price(products))

# [Liskov Substitution Principle (LSP)] Download the python file from this link. In this file, there is an implementation of a banking system for account handling. 
# There is a savings account and a checking account class. The checking account inherits the savings account as both have the same functionality and the checking account 
# allows overdrafts (allow processing transactions even if there is not sufficient balance). Redesign this program to follow the  
# Liskov Substitution Principle (LSP) principle which represents that “objects should be replaceable by their subtypes without altering how the program works”. 

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance) -> None:
        super().__init__(balance)

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)
    
#[Interface Segregation Principle (ISP)] Suppose we have an interface called PaymentProcessor that defines methods for processing payments and refunds. 
# Then we have a class called OnlinePaymentProcessor that implements the PaymentProcessor interface. 
# However, some parts of our system only need to process payments and do not handle refunds. 
# Redesign this program to follow the  Interface Segregation Principle (ISP) principle which represents that “Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.” 
# (Hint: Create two different classes in which one class use interfaces for process payment and another class can process and refund payment both)

class PaymentProcessor(ABC):
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

class BasicPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

online_p = OnlinePaymentProcessor()
basic_p = BasicPaymentProcessor()

online_p.process_payment(50)
online_p.process_refund(50)

basic_p.process_payment(5)

# [Dependency Inversion Principle (DIP)] Download the python file from this link. Suppose we have a NotificationService class that is responsible for sending notifications. 
# The NotificationService class directly depends on the EmailSender class to send emails.
# In this implementation, the NotificationService class directly depends on the EmailSender class, which violates the Dependency Inversion Principle. 
# The high-level NotificationService should not depend on the low-level EmailSender, as it tightly couples the classes together.
# Redesign this program to follow the  Dependency Inversion Principle (DIP) principle which represents that “Abstractions should not depend upon details. Details should depend upon abstractions.”

class NotificationSender(ABC):
    def send(self, recipient, subject, message):
        pass

class EmailSender(NotificationSender):
    def send(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def send_notification(self, recipient, subject, message):
        self.sender.send(recipient, subject, message)
        
# Using the NotificationService to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("user@example.com", "Notification" , "Hello, this is a notification!")
notification_service.send_notification("user2@example.com", "Introduction" , "Hello, this is an introduction!")