import pygame
import streamlit as st
from PIL import Image

# Initialize pygame
pygame.init()

# Define screen size
screen = pygame.display.set_mode((600, 400))

# Basic game loop (this is just an example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.display.flip()  # Update screen
    
    # Save the screen to a temporary image file
    pygame.image.save(screen, "screenshot.png")
    
    # Load the saved image with PIL
    img = Image.open("screenshot.png")
    
    # Display the image in Streamlit
    st.image(img, use_container_width=True)
