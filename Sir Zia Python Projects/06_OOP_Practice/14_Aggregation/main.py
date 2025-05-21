class Employee:
    def __init__(self, name):
        self.name = name

    def display_employee(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an existing Employee

    def display_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_employee()

# Example usage:
emp = Employee("Alice")
dept = Department("HR", emp)

dept.display_department()

# The Employee object 'emp' exists independently of Department
print("Employee still exists:", emp.name)
