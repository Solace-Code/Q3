class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")

# Example usage:
t1 = Teacher("Ms. Sara", "Mathematics")
