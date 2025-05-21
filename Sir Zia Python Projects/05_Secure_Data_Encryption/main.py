import streamlit as st
import hashlib

# In-memory data storage
stored_data = {}  # {encrypted_text: {"encrypted_text": encrypted_text, "passkey": hashed_passkey}}
failed_attempts = 0

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Get Caesar cipher shift from passkey hash
def get_shift_from_passkey(passkey):
    hashed = hash_passkey(passkey)
    return int(hashed[:2], 16) % 26  # Shift between 0-25

# Caesar cipher encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Caesar cipher decryption
def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

# Encrypt data with passkey
def encrypt_data(text, passkey):
    shift = get_shift_from_passkey(passkey)
    return caesar_encrypt(text, shift)

# Decrypt data with passkey
def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_passkey = hash_passkey(passkey)
    
    for key, value in stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            shift = get_shift_from_passkey(passkey)
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            failed_attempts = 0
            return decrypted_text
    
    failed_attempts += 1
    return None

# Streamlit UI
st.title("Secure Data Encryption System")

# Navigation menu
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Welcome to the Secure Data System")
    st.write("Use this app to securely store and retrieve data using unique passkeys.")

elif choice == "Store Data":
    st.subheader("Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("Data stored securely!")
        else:
            st.error("Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)
            if decrypted_text is not None:
                st.success(f"Decrypted Data: {decrypted_text}")
            else:
                st.error(f"Incorrect passkey! Attempts remaining: {3 - failed_attempts}")
                if failed_attempts >= 3:
                    st.warning("Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("Both fields are required!")

elif choice == "Login":
    st.subheader("Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Hardcoded master password for demo
            failed_attempts = 0
            st.success("Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("Incorrect password!")