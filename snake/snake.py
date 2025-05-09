import streamlit as st
import random
import time

# Grid size
WIDTH = 20
HEIGHT = 10

# Page setup
st.set_page_config(page_title="Snake Game", layout="centered")
st.title("🐍 Snake Game ")

# Initialize game state
if "snake" not in st.session_state:
    st.session_state.snake = [(WIDTH // 2, HEIGHT // 2)]
    st.session_state.food = (
        random.randint(0, WIDTH - 1),
        random.randint(0, HEIGHT - 1)
    )
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.game_over = False

# Predict next head position
def get_next_head():
    head_x, head_y = st.session_state.snake[0]
    direction = st.session_state.direction
    if direction == "UP":
        return (head_x, head_y - 1)
    elif direction == "DOWN":
        return (head_x, head_y + 1)
    elif direction == "LEFT":
        return (head_x - 1, head_y)
    else:  # RIGHT
        return (head_x + 1, head_y)

# Move snake forward
def move_snake():
    new_head = get_next_head()

    # Check for collisions BEFORE moving
    if (new_head in st.session_state.snake or
        not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)):
        st.session_state.game_over = True
        st.rerun()  # 🔁 Force immediate rerun to show Game Over
        return

    # Move
    st.session_state.snake.insert(0, new_head)

    # Eat food or move tail
    if new_head == st.session_state.food:
        st.session_state.score += 1
        while True:
            new_food = (
                random.randint(0, WIDTH - 1),
                random.randint(0, HEIGHT - 1)
            )
            if new_food not in st.session_state.snake:
                st.session_state.food = new_food
                break
    else:
        st.session_state.snake.pop()

# Draw the grid
def draw_board():
    board = [["⬛" for _ in range(WIDTH)] for _ in range(HEIGHT)]
    fx, fy = st.session_state.food
    board[fy][fx] = "🍎"
    for x, y in st.session_state.snake:
        if 0 <= y < HEIGHT and 0 <= x < WIDTH:
            board[y][x] = "🟩"
    return board

# Main game logic
if not st.session_state.game_over:
    move_snake()
    board = draw_board()
    for row in board:
        st.write("".join(row))
    st.write(f"Score: {st.session_state.score}")
else:
    st.error("💀 Game Over!")
    if st.button("🔁 Restart"):
        for key in ["snake", "food", "direction", "score", "game_over"]:
            del st.session_state[key]
        st.rerun()

# Controls (below the game)
st.write("### Controls")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"
with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"
with col3:
    st.write("")
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"

# Auto rerun
if not st.session_state.game_over:
    time.sleep(0.4)
    st.rerun()
