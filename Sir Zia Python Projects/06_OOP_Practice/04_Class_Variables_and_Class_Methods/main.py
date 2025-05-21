class Bank:
    bank_name = "Default Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change class variable using cls

    def display_bank(self):
        print("Bank Name:", self.bank_name)

# Example usage:
customer1 = Bank()
customer2 = Bank()

print("Before changing bank name:")
customer1.display_bank()
customer2.display_bank()

# Change bank name using class method
Bank.change_bank_name("National Bank")

print("\nAfter changing bank name:")
customer1.display_bank()
customer2.display_bank()
