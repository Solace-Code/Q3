class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage:
product = Product(100)
print("Price:", product.price)  # Gets price

product.price = 150  # Sets price
print("Updated Price:", product.price)

del product.price  # Deletes price
