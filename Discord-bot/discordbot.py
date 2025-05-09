import discord
from discord.ext import commands
import streamlit as st
import asyncio
import threading
import os
import signal  # Add this line to import the signal module

# Hardcoded Discord Bot Token
DISCORD_BOT_TOKEN = "Add Your Token"  # Replace with your actual bot token

if DISCORD_BOT_TOKEN is None:
    raise ValueError("Bot token not found. Please set the DISCORD_BOT_TOKEN variable.")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your friendly bot!")

@bot.command()
async def bot_status(ctx):
    await ctx.send(f"Bot is online and running as {bot.user}!")

# Function to start the bot
def run_bot():
    bot.run(DISCORD_BOT_TOKEN)

# Function to stop the bot (works in a Streamlit app with some limitations)
def stop_bot():
    os.kill(os.getpid(), signal.SIGINT)  # Simulate bot shutdown by sending SIGINT to the process

# Streamlit UI setup
st.title("Discord Bot Control Panel")
st.write("Welcome to the interactive Discord Bot Control Panel!")

st.markdown("""
    <style>
        .stButton>button {
            background-color: #008CBA;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px;
            transition: transform 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Start bot button
if st.button("Start Bot"):
    st.write("Starting bot... please wait!")
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    st.success("Bot is now running in the background! You can interact with it on Discord.")

# Stop bot button (just stops the process for this Streamlit app)
if st.button("Stop Bot"):
    st.write("Stopping bot...")
    stop_bot()
    st.success("Bot has been stopped.")

# Text input for bot commands
command = st.text_input("Enter command to send to bot", "")

if command:
    if command.lower() == "hello":
        st.write("Sending hello command to bot...")

        async def send_hello():
            await bot.wait_until_ready()
            channel = bot.get_channel()  # Replace with actual channel ID
            if channel:
                await channel.send("Hello from Streamlit!")

        asyncio.run(send_hello())
    else:
        st.write(f"Unknown command: {command}")

# Input field styling
st.markdown("""
    <style>
        .stTextInput>div>input {
            padding: 10px;
            font-size: 16px;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
