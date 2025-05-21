import streamlit as st
import hashlib


# ===============================
# Initialization
# ===============================
if "KEY" not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.KEY)

if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# ===============================
# Utility Functions
# ===============================
def hash_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text: str, passkey: str) -> str:
    return st.session_state.cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text: str, passkey: str):
    hashed_passkey = hash_passkey(passkey)
    data_entry = st.session_state.stored_data.get(encrypted_text)

    if data_entry and data_entry["passkey"] == hashed_passkey:
        st.session_state.failed_attempts = 0
        return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()

    st.session_state.failed_attempts += 1
    return None

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Secure Data Encryption", layout="centered")
st.title("Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# ===============================
# Pages
# ===============================

if choice == "Home":
    st.subheader("Welcome to the Secure Data System")
    st.write("This application lets you securely store and retrieve text data using a unique passkey.")
    st.write("Encryption is performed using Fernet from the cryptography library.")

elif choice == "Store Data":
    st.subheader("Store Data")
    user_data = st.text_area("Enter the text to encrypt:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt and Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("Data encrypted and stored successfully.")
            st.text_area("Encrypted Text (Save this to retrieve your data):", value=encrypted_text)
        else:
            st.error("Please enter both the text and the passkey.")

elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3:
        st.warning("Too many failed attempts. Redirecting to login...")
        st.switch_page("Login")

    st.subheader("Retrieve Data")
    encrypted_text = st.text_area("Enter the encrypted text:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success("Decryption successful.")
                st.text_area("Decrypted Text:", value=result)
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"Incorrect passkey. Attempts remaining: {remaining}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("Redirecting to Login page.")
                    st.experimental_rerun()
        else:
            st.error("Please fill in both fields.")

elif choice == "Login":
    st.subheader("Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.success("Reauthorized successfully. Returning to Retrieve Data page.")
            st.experimental_rerun()
        else:
            st.error("Incorrect master password.")