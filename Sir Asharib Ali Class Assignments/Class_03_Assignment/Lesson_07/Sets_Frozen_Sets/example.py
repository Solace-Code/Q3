# Set (mutable, no duplicates)
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)  # Duplicate 3 is removed

numbers.add(5)
print("After adding 5:", numbers)

# Frozenset (immutable)
frozen_numbers = frozenset([1, 2, 3, 4])
print("Frozenset:", frozen_numbers)

# You can't do frozen_numbers.add(6) — it will raise an error
