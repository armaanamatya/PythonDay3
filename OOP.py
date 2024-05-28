#OOP
#Create a Python class to represent a University. The university should have attributes like name, location, and a list of departments. 
# Implement encapsulation to protect the internal data of the University class. Create a Department class that inherits from the University class. 
# The Department class should have attributes like department name, head of the department, and a list of courses offered. Implement polymorphism by defining a common method for both the University and Department classes to display their details. 

class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def name(self):
        return self.__name
    
    def location(self):
        return self.__location
    
    def departments(self):
        return self.__departments

    def add_department(self, department):
        if isinstance(department, Department):
            self.__departments.append(department)

    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")

class Department(University):
    def __init__(self, name, location, department_name, head_of_department):
        super().__init__(name, location)
        self.__department_name = department_name
        self.__head_of_department = head_of_department
        self.__courses = []

    def department_name(self):
        return self.__department_name

    def head_of_department(self):
        return self.__head_of_department
    
    def courses(self):
        return self.__courses

    def add_course(self, course):
        self.__courses.append(course)

    def display_details(self):
        print(f"Department Name: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses:
            print(f" - {course}")

uni = University("UTAustin", "Austin")
dept1 = Department("UTAustin", "Austin", "Computer Science", "Dr. Heather")
dept1.add_course("Data Structures and Algorithms")
dept1.add_course("Machine Learning")

dept2 = Department("UTAustin", "Austin", "Mathematics", "Dr. Drew")
dept2.add_course("Algebra 1")
dept2.add_course("Algebra 2")

uni.add_department(dept1)
uni.add_department(dept2)

uni.display_details() 
dept1.display_details()
dept2.display_details()

# Build a Python class to represent a simple banking system. Create a class for a BankAccount, and another for Customer. 
# The BankAccount class should have a constructor to initialize the account details (account number, balance, account type). 
# The Customer class should have a constructor to set the customer's details (name, age, address) and create a BankAccount object for each customer. 
# Implement a destructor for both classes to display a message when objects are destroyed.

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        print(f"BankAccount {self.account_number} created.")

    def __del__(self):
        print(f"BankAccount {self.account_number} destroyed.")

class Customer:
    def __init__(self, name, age, address, account_number, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)
        print(f"Customer {self.name} created.")

    def __del__(self):
        print(f"Customer {self.name} destroyed.")
        del self.bank_account

customer1 = Customer("Armaan Amatya", 19, "Some street", "1001", 5000, "Savings")
customer2 = Customer("Ram Shyam", 28, "Some other street", "1002", 3000, "Checking")

del customer1
del customer2
