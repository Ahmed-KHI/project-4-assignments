import streamlit as st

# Initialize session state if not already present
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False

# Quiz questions
questions = [
    ("What will be the output of `print(2 * 3)`?", ["5", "6", "8", "9"], "6"),
    ("Which keyword is used to define a function in Python?", ["def", "func", "define", "lambda"], "def"),
    ("What is the result of `len([1, 2, 3])`?", ["2", "3", "4", "None"], "3"),
    ("Which of these data types is immutable in Python?", ["List", "Dictionary", "Tuple", "Set"], "Tuple"),
    ("How do you write a comment in Python?", ["// comment", "# comment", "/* comment */", "-- comment"], "# comment")
]

total_questions = len(questions)

# Get user details
st.title("🔥 Python Quiz Challenge! 🎯")
name = st.text_input("📝 Enter your Name:")
roll_number = st.text_input("🔢 Enter your Roll Number:")

if name and roll_number:
    st.write(f"👋 Welcome, **{name}**! 🎉 (Roll Number: {roll_number})")

    if st.session_state.current_question < total_questions:
        question, options, correct_answer = questions[st.session_state.current_question]

        st.subheader(f"📌 Question {st.session_state.current_question + 1} of {total_questions}")
        st.write(f"**{question}**")  # Display the question
        answer = st.radio("💡 Choose the correct answer:", options, key=f"q{st.session_state.current_question}")

        if st.button("✅ Submit Answer"):
            if answer == correct_answer:
                st.session_state.score += 1
                st.success("🎉 Correct! Well done! ✅")
            else:
                st.error("❌ Oops! That's incorrect.")

            st.session_state.current_question += 1
            st.rerun()
    else:
        st.subheader("🎊 Quiz Completed! 🎊")
        st.write(f"🎯 Your final score: **{st.session_state.score} / {total_questions}**")

        if st.session_state.score == total_questions:
            st.balloons()
            st.success("🌟 Perfect Score! You're a Python Pro! 🐍🔥")
        elif st.session_state.score > total_questions // 2:
            st.success("👍 Great Job! Keep Practicing! 💪")
        else:
            st.warning("📚 Keep Learning! You can do even better! 🚀")

        if st.button("🔄 Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.rerun()