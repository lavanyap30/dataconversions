import streamlit as st

# Function to convert data types
def convert_data_type(value, from_type, to_type):
    try:
        # Convert input value to the 'from' data type
        if from_type == 'int':
            value = int(value)
        elif from_type == 'float':
            value = float(value)
        elif from_type == 'str':
            value = str(value)
        elif from_type == 'bool':
            if value.lower() in ['true', '1', 't', 'yes', 'y']:
                value = True
            elif value.lower() in ['false', '0', 'f', 'no', 'n']:
                value = False
            else:
                raise ValueError("Cannot convert to boolean.")
        elif from_type == 'list':
            value = eval(value)
            if not isinstance(value, list):
                raise ValueError("Input is not a valid list.")
        elif from_type == 'tuple':
            value = eval(value)
            if not isinstance(value, tuple):
                raise ValueError("Input is not a valid tuple.")
        elif from_type == 'set':
            value = eval(value)
            if not isinstance(value, set):
                raise ValueError("Input is not a valid set.")
        elif from_type == 'dict':
            value = eval(value)
            if not isinstance(value, dict):
                raise ValueError("Input is not a valid dictionary.")
        else:
            raise ValueError("Invalid from_type specified.")

        # Convert 'from' data type to 'to' data type
        if to_type == 'int':
            result = int(value)
        elif to_type == 'float':
            result = float(value)
        elif to_type == 'str':
            result = str(value)
        elif to_type == 'bool':
            result = bool(value)
        elif to_type == 'list':
            result = list(value)
        elif to_type == 'tuple':
            result = tuple(value)
        elif to_type == 'set':
            result = set(value)
        elif to_type == 'dict':
            if isinstance(value, (list, tuple)):
                if all(isinstance(item, (list, tuple)) and len(item) == 2 for item in value):
                    result = dict(value)
                else:
                    raise ValueError("Cannot convert to dictionary. Needs a list or tuple of key-value pairs.")
            else:
                result = dict(value)
        else:
            raise ValueError("Invalid to_type specified.")

        return result, None  # Return result and no error message

    except Exception as e:
        return None, str(e)  # Return no result and an error message

# Streamlit UI components
st.title("Python Data Type Converter")

st.write("Convert values between different Python data types, including collections.")

# Input fields
from_type = st.selectbox("From Data Type", ['int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict'])
to_type = st.selectbox("To Data Type", ['int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict'])
value = st.text_input("Value to Convert", "Enter value according to selected 'From Data Type'")

# Conversion button
if st.button("Convert"):
    if value.strip() == "":
        st.error("Please enter a value to convert.")
    else:
        # Perform the conversion
        result, error = convert_data_type(value, from_type, to_type)
        
        # Display result or error
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Converted value: {result} (Type: {to_type})")
