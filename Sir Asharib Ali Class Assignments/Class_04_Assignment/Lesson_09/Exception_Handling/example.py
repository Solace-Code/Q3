try:
    # Code that may cause an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    # This block runs if division by zero is attempted
    print("Error: Cannot divide by zero.")

except ValueError:
    # This block runs if input is not an integer
    print("Error: Please enter valid numbers.")

except Exception as e:
    # This catches any other exception
    print("Unexpected error:", e)

finally:
    # This block always runs, whether there is an error or not
    print("Execution complete.")
