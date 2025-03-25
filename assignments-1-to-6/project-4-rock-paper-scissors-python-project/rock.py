import streamlit as st
import random

st.title("🪨📄✂️ Rock, Paper, Scissors Game!")

# Initialize session state for scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.rounds = 0

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("Choose one:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.subheader(f"🤖 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        st.session_state.ties += 1
        st.warning("😲 It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.session_state.user_score += 1
        st.success("🎉 You win!")
    else:
        st.session_state.computer_score += 1
        st.error("💀 You lose!")

    st.session_state.rounds += 1

    # Display scoreboard
    st.subheader("📊 Scoreboard")
    st.write(f"🧑 Your Score: {st.session_state.user_score}")
    st.write(f"🤖 Computer Score: {st.session_state.computer_score}")
    st.write(f"🔄 Ties: {st.session_state.ties}")

    # Best of 5 Winner
    if st.session_state.rounds >= 5:
        st.subheader("🎯 Best of 5 Result:")
        if st.session_state.user_score > st.session_state.computer_score:
            st.success("🏆 Congratulations! You won the Best of 5!")
        elif st.session_state.user_score < st.session_state.computer_score:
            st.error("💀 Computer won the Best of 5! Better luck next time!")
        else:
            st.warning("😲 Best of 5 ended in a tie!")

# Restart game button
if st.button("Restart Game 🔄"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.rounds = 0
    st.rerun()