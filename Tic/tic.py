
import streamlit as st

st.title("Tic-Tac-Toe")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [None] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "last_move" not in st.session_state:
    st.session_state.last_move = -1

# Function to check for a winner
def check_win(board):
    combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
    for a, b, c in combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

# Function to reset the game
def reset_game():
    st.session_state.board = [None] * 9
    st.session_state.turn = "X"
    st.session_state.game_over = False
    st.session_state.last_move = -1

# Handle last move if any
if st.session_state.last_move != -1 and not st.session_state.game_over:
    idx = st.session_state.last_move
    if st.session_state.board[idx] is None:
        st.session_state.board[idx] = st.session_state.turn
        winner = check_win(st.session_state.board)
        if winner:
            st.success(f"{winner} wins!")
            st.session_state.game_over = True
        elif None not in st.session_state.board:
            st.info("It's a tie!")
            st.session_state.game_over = True
        else:
            st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
    st.session_state.last_move = -1  # Reset after processing

# Display the board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        idx = i * 3 + j
        label = st.session_state.board[idx] if st.session_state.board[idx] else " "
        if cols[j].button(label, key=f"cell_{idx}"):
            if not st.session_state.game_over and st.session_state.board[idx] is None:
                st.session_state.last_move = idx
                st.rerun()  # << Fixed here

# Show current turn
if not st.session_state.game_over:
    st.info(f"Current Turn: {st.session_state.turn}")

# Reset button
st.markdown("---")
if st.button("Reset Game"):
    reset_game()
    st.rerun()
