class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance with factor 5
mul = Multiplier(5)

# Test if object is callable
print(callable(mul))  # True

# Call the object like a function
result = mul(10)
print("Result:", result)
