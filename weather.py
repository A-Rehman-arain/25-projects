
import streamlit as st
import requests

# Function to get weather data
def get_weather(city):
    api_key = 'b3610a29e28146328df172014250205'  # 🔁 Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        return {"cod": "error", "message": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"cod": "error", "message": f"An error occurred: {str(e)}"}

# Streamlit UI
st.title("🌦️ Weather Checker")

city = st.text_input("Enter a city name")

if city:
    data = get_weather(city)

    if data.get('cod') == 200:
        weather = data['weather'][0]['description'].title()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15

        st.subheader(f"📍 Weather in {city.title()}")
        st.write(f"🌤 Condition: {weather}")
        st.write(f"🌡 Temperature: {temp_celsius:.2f} °C")
    elif data.get('cod') == 'error':
        st.error(f"⚠️ {data.get('message')}")
    else:
        st.warning("⚠️ City not found. Please check the city name.")
