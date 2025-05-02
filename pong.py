import streamlit as st
import random

st.title("🏓 Pong Simulation (Manual Frame Update)")

# Initialize session state
if "ball_x" not in st.session_state:
    st.session_state.ball_x = 50
    st.session_state.ball_y = 50
    st.session_state.dx = random.choice([-1, 1])
    st.session_state.dy = random.choice([-1, 1])
    st.session_state.score = [0, 0]
    st.session_state.running = False

# Show score and ball position
st.write(f"Player 1: {st.session_state.score[0]} | Player 2: {st.session_state.score[1]}")
st.write(f"Ball position: ({st.session_state.ball_x}, {st.session_state.ball_y})")

# Start game
if st.button("Start Game"):
    st.session_state.running = True

# Next frame button (manual update)
if st.session_state.running:
    if st.button("➡️ Next Frame"):
        st.session_state.ball_x += st.session_state.dx
        st.session_state.ball_y += st.session_state.dy

        # Bounce off left/right walls
        if st.session_state.ball_x <= 0 or st.session_state.ball_x >= 100:
            st.session_state.dx = -st.session_state.dx

        # Bounce off top/bottom walls
        if st.session_state.ball_y <= 0 or st.session_state.ball_y >= 100:
            st.session_state.dy = -st.session_state.dy

        st.write("Frame updated!")

# Reset game
if st.button("🔄 Reset Game"):
    st.session_state.ball_x = 50
    st.session_state.ball_y = 50
    st.session_state.dx = random.choice([-1, 1])
    st.session_state.dy = random.choice([-1, 1])
    st.session_state.running = False
    st.write("Game reset.")
