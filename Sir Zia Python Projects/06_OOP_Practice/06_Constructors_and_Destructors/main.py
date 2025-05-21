class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor message

    def __del__(self):
        print("Logger object destroyed.")  # Destructor message

# Example usage:
log = Logger()

# Manually deleting the object (optional)
del log
