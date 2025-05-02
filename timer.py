import streamlit as st
import time

st.title("Countdown Timer")

# Store timer state in session state to ensure it persists across reruns
if 'is_running' not in st.session_state:
    st.session_state.is_running = False  # Timer is not running initially
    st.session_state.timer_done = False  # Timer has not finished

# Input for minutes and seconds
minutes = st.number_input("Enter minutes:", min_value=0, max_value=60, value=0)
seconds = st.number_input("Enter seconds:", min_value=0, max_value=60, value=10)

# Start timer button
if st.button("Start Timer") and not st.session_state.is_running:
    total_seconds = minutes * 60 + seconds
    st.session_state.is_running = True
    st.session_state.timer_done = False
    timer_placeholder = st.empty()  # Placeholder for the countdown display

    for i in range(total_seconds, -1, -1):
        if not st.session_state.is_running:  # Check if the timer is stopped prematurely
            break
        mins, secs = divmod(i, 60)
        timer_placeholder.markdown(f"### ⏱️ {mins:02d}:{secs:02d}")
        time.sleep(1)

    # After the timer finishes
    st.session_state.is_running = False
    st.session_state.timer_done = True
    timer_placeholder.markdown("### ⏱️ Time's up!")

# Reset button to stop timer
if st.session_state.timer_done:
    if st.button("Reset Timer"):
        st.session_state.is_running = False
        st.session_state.timer_done = False
        st.rerun()  # Restart the app to reset the timer state

# If the timer is already running, display a message
if st.session_state.is_running:
    st.info("Timer is running...")  
