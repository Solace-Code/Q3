# password_strength_meter.py
import streamlit as st
import string

# Function to evaluate password strength
def check_password_strength(password: str):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Make your password at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("🔸 Include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("🔸 Include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("🔸 Include at least one digit (0-9).")

    if any(char in "!@#$%^&*" for char in password):
        score += 1
    else:
        feedback.append("🔸 Add a special character (!@#$%^&*).")

    return score, feedback

# Streamlit app layout
def main():
    st.title("🔐 Password Strength Meter")

    password = st.text_input("Enter your password", type="password")

    if password:
        score, feedback = check_password_strength(password)

        st.markdown("### 🔎 Strength Evaluation")

        if score <= 2:
            st.error("❌ Weak Password")
        elif score <= 4:
            st.warning("⚠️ Moderate Password")
        else:
            st.success("✅ Strong Password")

        st.markdown(f"**Score:** {score}/5")

        if score < 5:
            st.markdown("#### 💡 Suggestions to Improve:")
            for tip in feedback:
                st.write(tip)
        else:
            st.markdown("🎉 Great! Your password is strong and secure.")

if __name__ == "__main__":
    main()