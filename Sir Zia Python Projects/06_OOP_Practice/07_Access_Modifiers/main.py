class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected (convention)
        self.__ssn = ssn        # Private (name mangling)

# Create an instance
emp = Employee("John", 50000, "123-45-6789")

# Accessing public variable
print("Public - Name:", emp.name)  # ✅ Accessible

# Accessing protected variable
print("Protected - Salary:", emp._salary)  # ⚠️ Technically accessible, but should be treated as protected

# Accessing private variable
try:
    print("Private - SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Private - SSN: Cannot access directly:", e)

# Accessing private variable using name mangling
print("Private - SSN (via name mangling):", emp._Employee__ssn)  # ✅ Accessible with trick
