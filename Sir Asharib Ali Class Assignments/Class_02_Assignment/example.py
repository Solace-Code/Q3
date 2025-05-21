# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor division

# 2. Assignment Operators
print("\nAssignment Operators:")
x = 5
print("x =", x)
x += 3
print("x += 3 =>", x)
x -= 2
print("x -= 2 =>", x)
x *= 4
print("x *= 4 =>", x)
x /= 2
print("x /= 2 =>", x)
x %= 3
print("x %= 3 =>", x)
x **= 2
print("x **= 2 =>", x)
x //= 2
print("x //= 2 =>", x)

# 3. Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 4. Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 5. Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("x is z:", x is z)       # True, same object
print("x is y:", x is y)       # False, different objects
print("x is not y:", x is not y)

# 6. Membership Operators
print("\nMembership Operators:")
print("2 in x:", 2 in x)
print("4 not in x:", 4 not in x)

# 7. Bitwise Operators
print("\nBitwise Operators:")
a = 5   # 0101 in binary
b = 3   # 0011 in binary
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left shift
print("a >> 1 =", a >> 1) # Right shift
