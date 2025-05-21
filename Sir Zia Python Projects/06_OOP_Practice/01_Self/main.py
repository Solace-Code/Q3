class Student:
    def __init__(self, name, marks):
        self.name = name      # Using self to refer to instance variable
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Ali", 85)
student1.display()
