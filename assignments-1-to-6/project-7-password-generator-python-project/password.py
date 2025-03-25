import re
import random
import string
import streamlit as st

# Common weak passwords list 
BLACKLISTED_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123", "password123",
    "admin", "letmein", "welcome", "iloveyou", "monkey", "football"
]

# Scoring weights
WEIGHTS = {
    "length": 2,
    "uppercase": 1.5,
    "lowercase": 1,
    "digits": 1.5,
    "special": 2
}

# Store last 3 checked passwords
if "password_history" not in st.session_state:
    st.session_state.password_history = []

def generate_strong_password():
    length = random.randint(12, 16)
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passphrase():
    words = ["tiger", "rocket", "banana", "stream", "planet", "guitar", "vision", "jungle", "diamond", "python"]
    passphrase = "-".join(random.sample(words, 4))
    return passphrase.capitalize()

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in BLACKLISTED_PASSWORDS:
        return "❌ Very Weak (Blacklisted)", ["This password is too common. Please choose a more unique password."], 0

    if len(password) >= 8:
        score += WEIGHTS["length"]
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += WEIGHTS["uppercase"]
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += WEIGHTS["lowercase"]
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += WEIGHTS["digits"]
    else:
        feedback.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += WEIGHTS["special"]
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    max_score = sum(WEIGHTS.values())
    if score <= max_score * 0.3:
        strength = "🔴 Weak"
    elif score <= max_score * 0.6:
        strength = "🟡 Moderate"
    else:
        strength = "🟢 Strong"

    return strength, feedback, score / max_score

def main():
    st.set_page_config(page_title="🚀 Super Password Strength Checker")
    st.title("🔐 Password Strength Checker with Extra Features")

    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength"):
        if password:
            strength, feedback, score = check_password_strength(password)
            st.write(f"### Password Strength: {strength}")

            if strength == "🔴 Weak":
                st.error("Your password is weak. Consider these suggestions:")
                for tip in feedback:
                    st.write(f"- {tip}")
            else:
                st.success("Your password is strong! 👍")

            st.progress(score)  # Strength meter bar

            # Store password history
            st.session_state.password_history.insert(0, (password, strength))
            st.session_state.password_history = st.session_state.password_history[:3]
        else:
            st.warning("Please enter a password to check.")

    # Display last 3 checked passwords
    if st.session_state.password_history:
        st.write("## 🔄 Last 3 Checked Passwords")
        for idx, (pwd, strg) in enumerate(st.session_state.password_history, 1):
            st.write(f"{idx}. `{pwd}` ➝ {strg}")

    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.write(f"### Generated Strong Password: `{strong_password}`")

    if st.button("Generate Passphrase"):
        passphrase = generate_passphrase()
        st.write(f"### Generated Passphrase: `{passphrase}`")

if __name__ == "__main__":
    main()