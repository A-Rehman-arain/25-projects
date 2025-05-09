import streamlit as st
import string
import secrets

st.title("🔐 Secure Password Generator")

# Options
length = st.slider("Password length", 6, 32, 12)
include_special = st.checkbox("Include special characters (!@#...)", value=True)
avoid_ambiguous = st.checkbox("Avoid ambiguous characters (O, 0, l, I)", value=True)

# Character set
chars = string.ascii_letters + string.digits
if include_special:
    chars += string.punctuation

if avoid_ambiguous:
    ambiguous = 'O0lI|`\'"'
    chars = ''.join(c for c in chars if c not in ambiguous)

# Generate password
if st.button("Generate Password"):
    password = ''.join(secrets.choice(chars) for _ in range(length))
    st.success("Generated Password:")
    st.code(password, language='text')
