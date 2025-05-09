import streamlit as st
import numpy as np

# Initialize board
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((6, 7), int)  # 6 rows, 7 columns
    st.session_state.current_player = 1  # Player 1 starts (1 for red, 2 for yellow)
    st.session_state.game_over = False  # To track if the game is over

# Function to drop a disc in the selected column
def drop_disc(col):
    # Find the first empty row in the column
    for row in range(5, -1, -1):
        if st.session_state.board[row][col] == 0:
            st.session_state.board[row][col] = st.session_state.current_player
            return True  # Return True when the disc is successfully dropped
    return False  # Return False if the column is full

# Function to check if there's a winner
def check_winner():
    for row in range(6):
        for col in range(7):
            if st.session_state.board[row][col] == 0:
                continue
            player = st.session_state.board[row][col]
            # Check horizontal, vertical, and diagonal
            if col + 3 < 7 and all(st.session_state.board[row][col + i] == player for i in range(4)):
                return player
            if row + 3 < 6 and all(st.session_state.board[row + i][col] == player for i in range(4)):
                return player
            if row + 3 < 6 and col + 3 < 7 and all(st.session_state.board[row + i][col + i] == player for i in range(4)):
                return player
            if row - 3 >= 0 and col + 3 < 7 and all(st.session_state.board[row - i][col + i] == player for i in range(4)):
                return player
    return 0

# Function to handle game reset
def reset_game():
    st.session_state.board = np.zeros((6, 7), int)  # Reset the board
    st.session_state.current_player = 1  # Player 1 starts
    st.session_state.game_over = False  # Reset game over status
    st.rerun()  # Reload the app to reset the state

# Display the game board
if not st.session_state.game_over:
    for row in range(6):
        cols = st.columns(7)
        for col in range(7):
            with cols[col]:
                # Disable buttons in full columns
                if st.session_state.board[row][col] == 0:
                    button_label = ' '  # Empty cell
                    disabled = False
                else:
                    button_label = 'R' if st.session_state.board[row][col] == 1 else 'Y'
                    disabled = True  # Disable button if it's already filled

                if st.button(button_label, key=f'{row}-{col}', disabled=disabled):
                    if drop_disc(col):
                        st.session_state.current_player = 3 - st.session_state.current_player  # Switch player

    # Check for winner
    winner = check_winner()
    if winner:
        st.session_state.game_over = True
        st.write(f"Player {winner} wins!")
    elif np.all(st.session_state.board != 0):
        st.session_state.game_over = True
        st.write("It's a tie!")

    # Display the current player's turn
    current_player = 'Red' if st.session_state.current_player == 1 else 'Yellow'
    st.write(f"Current Player: {current_player}")

else:
    # Game over, offer restart button
    if st.button("Restart Game"):
        reset_game()  # Reset the game and reload the app
