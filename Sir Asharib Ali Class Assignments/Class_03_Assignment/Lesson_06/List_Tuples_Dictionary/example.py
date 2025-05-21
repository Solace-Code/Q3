# Lists
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

print("First fruit:", fruits[0])


# Tuples (immutable)
coordinates = (10, 20)
print("Tuple:", coordinates)
print("X coordinate:", coordinates[0])

# Tuple unpacking
x, y = coordinates
print("x =", x, ", y =", y)


# Dictionary
student = {
    "name": "Ali",
    "age": 21,
    "course": "Python"
}

print("Student Info:", student)
print("Name:", student["name"])

student["age"] = 22  # Update value
print("Updated age:", student["age"])

student["grade"] = "A"  # Add new key
print("After adding grade:", student)