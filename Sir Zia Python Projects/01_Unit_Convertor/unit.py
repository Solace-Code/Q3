import streamlit as st

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

# Streamlit UI
st.title("Unit Converter")

category = st.selectbox("Select a category", ("Length", "Weight", "Temperature", "Volume"))

if category == "Length":
    units = ["meter", "kilometer", "foot", "mile"]
    convert_func = convert_length
elif category == "Weight":
    units = ["kilogram", "gram", "pound"]
    convert_func = convert_weight
elif category == "Temperature":
    units = ["celsius", "fahrenheit"]
    convert_func = convert_temperature
elif category == "Volume":
    units = ["liter", "milliliter", "gallon"]
    convert_func = convert_volume

from_unit = st.selectbox("From unit", units)
to_unit = st.selectbox("To unit", units)
value = st.number_input("Enter the value to convert", format="%.4f")

if st.button("Convert"):
    try:
        result = convert_func(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")
