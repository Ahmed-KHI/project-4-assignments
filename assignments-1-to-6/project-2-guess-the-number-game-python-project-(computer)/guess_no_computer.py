import streamlit as st
import random

# Initialize session state variables
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎲 Guess the Number Game! 🎯")

st.write("I have selected a number between **1 and 100**. Try to guess it!")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.warning("🔼 Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.warning("🔽 Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Restart Game"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()