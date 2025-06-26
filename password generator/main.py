import streamlit as st 
import random 
import string

def password_generator(length, use_digits, use_special):

    character = string.ascii_letters

    if use_digits:
        character += string.digits

    if use_special:
        character += string.punctuation

    return ''.join(random.choice(character) for _ in range(length))


st.title("PASSWORD GENERATOR")
length = st.slider("select password length", min_value=6, max_value=32)
use_digit = st.checkbox("include digits")
use_special = st.checkbox("include special")

if st.button("GENERATE_PASSWORD"):
    password = password_generator(length, use_digit, use_special)
    st.write(f"generated password: {password}")
