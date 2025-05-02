import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Web Scraping Tool')

url = st.text_input('Enter URL to scrape:', '')

if url:
    # Make the HTTP request to fetch the page content
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check and display the page title
        st.subheader('Page Title:')
        if soup.title:
            st.write(soup.title.string)
        else:
            st.write("No title tag found")

        # Display extracted text (all paragraphs)
        st.subheader('Extracted Text:')
        paragraphs = soup.find_all('p')
        if paragraphs:
            for para in paragraphs:
                st.write(para.text)
        else:
            st.write("No paragraphs found on this page.")