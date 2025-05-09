import streamlit as st
import random

st.set_page_config(page_title="Hangman", page_icon="🎯", layout="centered")
st.title("🎯 Hangman Game")

# List of words
word_list = ['python', 'streamlit', 'discord', 'hangman']

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_list)
    st.session_state.guessed = set()
    st.session_state.attempts = 6
    st.session_state.game_over = False

# Display the word with underscores
display_word = ' '.join([letter if letter in st.session_state.guessed else '_' for letter in st.session_state.word])
st.subheader(f"Word: {display_word}")

# Guess input
if not st.session_state.game_over:
    guess = st.text_input("Guess a letter:", max_chars=1)

    if guess:
        guess = guess.lower()

        if not guess.isalpha():
            st.warning("Please enter a valid letter.")
        elif guess in st.session_state.guessed:
            st.info("You already guessed that letter.")
        else:
            st.session_state.guessed.add(guess)

            if guess not in st.session_state.word:
                st.session_state.attempts -= 1
                st.error(f"Wrong guess! '{guess}' is not in the word.")

# Game status check
if all(letter in st.session_state.guessed for letter in st.session_state.word):
    st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
    st.session_state.game_over = True
elif st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word}")
    st.session_state.game_over = True
else:
    st.write(f"🧠 Attempts left: **{st.session_state.attempts}**")
    st.write(f"🔤 Letters guessed: {', '.join(sorted(st.session_state.guessed))}")

# Reset game
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        for key in ["word", "guessed", "attempts", "game_over"]:
            st.session_state.pop(key)
        st.rerun()
