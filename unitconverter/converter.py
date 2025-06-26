import streamlit as st  # Import Streamlit library for web app

def convert_unit(value, unit_from, unit_to):
    # Dictionary holding conversion rates between units
    conversions = {
        "meter": {"kilometer": 0.001, "meter": 1},      # 1 meter = 0.001 kilometer, 1 meter = 1 meter
        "kilometer": {"meter": 1000, "kilometer": 1},   # 1 kilometer = 1000 meters, 1 kilometer = 1 kilometer
        "gram": {"kilogram": 0.001, "gram": 1},         # 1 gram = 0.001 kilogram, 1 gram = 1 gram
        "kilogram": {"gram": 1000, "kilogram": 1},      # 1 kilogram = 1000 grams, 1 kilogram = 1 kilogram
    }
    # Check if conversion is supported
    if unit_from in conversions and unit_to in conversions[unit_from]:
        conversion = conversions[unit_from][unit_to]  # Get conversion rate
        return value * conversion  # Return converted value
    else:
        return "conversion not supported"  # Return error if conversion not possible

st.title("unit_converter")  # Set the title of the web app

value = st.number_input("Enter the value", min_value=1.0,step=1.0)  # Input box for value to convert
unit_from = st.selectbox("convert from", ["meter", "kilometer", "gram", "kilogram"])  # Dropdown for source unit
unit_to = st.selectbox("convert to", ["meter", "kilometer", "gram", "kilogram"])  # Dropdown for target unit

if st.button("convert"):  # Button to trigger conversion
    result = convert_unit(value, unit_from, unit_to)  # Call conversion function
    st.write(f"unit converted: {result}")  # Display result
    