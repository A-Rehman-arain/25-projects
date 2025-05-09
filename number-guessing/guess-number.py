import streamlit as st

st.set_page_config(page_title="Guess the Number", page_icon="🎯", layout="centered")
st.title("🎯 Guess the Number (Computer Guesses)")

# Initialize state variables
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 1

# Check for invalid logic
if st.session_state.low > st.session_state.high:
    st.error("🚨 Oops! Something went wrong. Maybe inconsistent responses? Please restart the game.")
    if st.button("🔁 Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
else:
    # Game is in progress
    if not st.session_state.game_over:
        st.subheader(f"🤖 Is your number **{st.session_state.guess}**?")
        st.caption(f"🔢 Attempt #{st.session_state.attempts}")

        col1, col2, col3 = st.columns(3)

        if col1.button("Too Low"):
            st.session_state.low = st.session_state.guess + 1
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
            st.session_state.attempts += 1
            st.rerun()

        elif col2.button("Too High"):
            st.session_state.high = st.session_state.guess - 1
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
            st.session_state.attempts += 1
            st.rerun()

        elif col3.button("Correct!"):
            st.session_state.game_over = True
            st.balloons()
            st.success(f"🎉 Yay! I guessed it right in {st.session_state.attempts} attempts. It was **{st.session_state.guess}**.")

    # Game over state
    if st.session_state.game_over:
        if st.button("🔁 Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
