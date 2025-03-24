import re
import streamlit as st

def check_password_strength(password):
    """
    Function to check the strength of a password.
    """
    if len(password) < 8:
        return "❌ Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "❌ Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "❌ Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "❌ Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "⚠️ Medium: Add special characters to make your password stronger."
    
    return "✅ Strong: Your password is secure!"

# Streamlit UI
st.title("🔐 Password Strength Checker")

st.subheader("Tips for Secure Password:")
st.text("A Secure Password can include :")
st.text("1. 8 characters long ✅")
st.text("2. at least one number ✅")
st.text("3. one uppercase letter ✅")
st.text("4. one lowercase letter ✅")
st.text("5. special characters E.G: #$%^&* ✅")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        result = check_password_strength(password)
        st.markdown(f"**{result}**")
    else:
        st.warning("Please enter a password to check its strength.")
