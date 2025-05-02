import pygame
import streamlit as st
import numpy as np
import io
from PIL import Image

# Initialize pygame
pygame.init()

# Set up game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game state initialization
game_board = np.zeros((20, 10))  # 20 rows, 10 columns
current_piece = np.array([[1, 1, 1], [0, 1, 0]])  # T-shape piece

# Function to draw the game board
def draw_board():
    screen.fill(BLACK)
    for row in range(20):
        for col in range(10):
            if game_board[row][col]:
                pygame.draw.rect(screen, GREEN, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

# Convert pygame surface to image to display in Streamlit
def pygame_to_streamlit():
    # Save the Pygame screen to a temporary surface
    pygame.image.save(screen, "temp_screenshot.png")
    
    # Open the image with PIL and return it
    img = Image.open("temp_screenshot.png")
    return img

# Function to update the game state (e.g., move the current piece)
def update_game_state():
    # Example: Move the piece down for simplicity
    global game_board
    for row in range(18, -1, -1):
        for col in range(10):
            if game_board[row][col]:
                game_board[row + 1][col] = game_board[row][col]
                game_board[row][col] = 0
    draw_board()

# Running the game inside Streamlit
if st.button("Start Tetris"):
    draw_board()
    st.image(pygame_to_streamlit(), use_container_width=True)
    pygame.time.delay(500)  # Wait before the next frame
    update_game_state()
    st.image(pygame_to_streamlit(), use_container_width=True)  # Display updated frame
