import streamlit as st
import random

# List of words
word_list = ['python', 'streamlit', 'developer', 'hangman', 'coding']

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_list)
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6

word = st.session_state.word

def display_word():
    return ' '.join([letter if letter in st.session_state.guessed_letters else '_' for letter in word])

st.title("🕵️ Hangman Game")
st.write("Guess the word letter by letter!")

# Display word progress
st.subheader(display_word())
st.write(f"Attempts Left: {st.session_state.attempts}")

guess = st.text_input("Enter a letter:", max_chars=1).lower()
if st.button("Submit Guess"):
    if guess and guess.isalpha():
        if guess in st.session_state.guessed_letters:
            st.warning("You already guessed this letter!")
        else:
            st.session_state.guessed_letters.append(guess)
            if guess not in word:
                st.session_state.attempts -= 1
    st.rerun()  # ✅ Updated from st.experimental_rerun()

if '_' not in display_word():
    st.success(f"🎉 Congrats! You guessed the word: {word}")
    if st.button("Play Again"):
        st.session_state.word = random.choice(word_list)
        st.session_state.guessed_letters = []
        st.session_state.attempts = 6
        st.rerun()  # ✅ Updated from st.experimental_rerun()

if st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The word was: {word}")
    if st.button("Try Again"):
        st.session_state.word = random.choice(word_list)
        st.session_state.guessed_letters = []
        st.session_state.attempts = 6
        st.rerun()  # ✅ Updated from st.experimental_rerun()