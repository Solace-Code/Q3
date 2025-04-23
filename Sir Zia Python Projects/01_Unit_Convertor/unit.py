def convert_length(value, from_unit, to_unit):
    units = {
        'meter': 1,
        'kilometer': 1000,
        'foot': 0.3048,
        'mile': 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        'kilogram': 1,
        'gram': 0.001,
        'pound': 0.453592
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    if from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    raise ValueError('Unsupported temperature conversion')

def convert_volume(value, from_unit, to_unit):
    units = {
        'liter': 1,
        'milliliter': 0.001,
        'gallon': 3.78541
    }
    return value * units[from_unit] / units[to_unit]

def main():
    print("Welcome to the Unit Converter\n")
    print("Select a category:")
    print("1. Length (meter, kilometer, foot, mile)")
    print("2. Weight (kilogram, gram, pound)")
    print("3. Temperature (celsius, fahrenheit)")
    print("4. Volume (liter, milliliter, gallon)\n")

    category_input = input("Enter category (length/weight/temperature/volume): ").strip().lower()

    if category_input == "length":
        print("\nAvailable units: meter, kilometer, foot, mile")
    elif category_input == "weight":
        print("\nAvailable units: kilogram, gram, pound")
    elif category_input == "temperature":
        print("\nAvailable units: celsius, fahrenheit")
    elif category_input == "volume":
        print("\nAvailable units: liter, milliliter, gallon")
    else:
        print("Invalid category. Please restart the program.")
        return

    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()

    try:
        value = float(input("Enter the value to convert: "))

        if category_input == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif category_input == 'weight':
            result = convert_weight(value, from_unit, to_unit)
        elif category_input == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        elif category_input == 'volume':
            result = convert_volume(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid category")

        print(f"\nResult: {value} {from_unit} = {result:.4f} {to_unit}")

    except KeyError:
        print("Invalid unit entered.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
