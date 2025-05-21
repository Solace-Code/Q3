class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Create an object of D
d = D()

# Call show() and observe which method runs
d.show()

# Optional: Print the MRO for class D
print("MRO for class D:", [cls.__name__ for cls in D.__mro__])
