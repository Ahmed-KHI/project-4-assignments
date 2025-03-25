import streamlit as st
import random

st.title("🤖 Guess the Number Game (User)")
st.write("I am thinking of a number between 1 and 100. Try to guess it!")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    
    if user_guess < st.session_state.number:
        st.warning("⬆️ Too Low! Try Again.")
    elif user_guess > st.session_state.number:
        st.warning("⬇️ Too High! Try Again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number} in {st.session_state.attempts} attempts! 🎯")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()