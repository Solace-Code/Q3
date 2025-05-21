# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Writing multiple lines is easy in Python.\n")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to the file
with open("sample.txt", "a") as file:
    file.write("This line was added later.\n")

# Reading again to show updated content
with open("sample.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated File Content:\n", updated_content)
