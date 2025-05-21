class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car has started.")

# Example usage:
car1 = Car("Toyota")

# Accessing public variable
print("Car Brand:", car1.brand)

# Calling public method
car1.start()
