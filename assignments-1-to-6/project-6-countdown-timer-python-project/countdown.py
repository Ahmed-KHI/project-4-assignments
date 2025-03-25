import streamlit as st
import time

# Title
st.title("⏳ Countdown Timer")

# Initialize session state
if 'time_left' not in st.session_state:
    st.session_state.time_left = 0
    st.session_state.running = False
    st.session_state.total_time = 0  # Store the total time

# User input
if not st.session_state.running:
    seconds = st.number_input("⏲️ Enter countdown time (in seconds):", min_value=1, step=1)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start Countdown"):
            st.session_state.time_left = seconds
            st.session_state.total_time = seconds  # Store for progress bar
            st.session_state.running = True
            st.rerun()

# Timer Logic
if st.session_state.running:
    progress_bar = st.progress(0)
    
    while st.session_state.time_left > 0:
        st.write(f"⏳ Time Left: **{st.session_state.time_left}** seconds ⌛")
        
        # Calculate progress
        progress = (1 - (st.session_state.time_left / st.session_state.total_time))
        progress_bar.progress(progress)
        
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

    # Timer Complete
    st.session_state.running = False
    progress_bar.progress(1)  # Complete progress bar
    st.success("🎉 ⏰ Time's up! 🚀")

    # Beep sound (Optional: Works only in local execution)
    st.write("\a")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Restart Timer"):
            st.session_state.time_left = 0
            st.session_state.running = False
            st.session_state.total_time = 0
            st.rerun()