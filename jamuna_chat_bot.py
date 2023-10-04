# -*- coding: utf-8 -*-
"""jamuna Chat bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1979oAyw-jpE7O37NsQA2_1_IH7Tf-k2e
"""

import openai
import requests
from bs4 import BeautifulSoup
#API key
openai.api_key = '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'

# Function to chat
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to fetch website
def extract_information(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting all the text within <h1> tags
        headings = soup.find_all('h1')
        for heading in headings:
            print("Heading:", heading.text)

        # Extracting all the links in the page
        links = soup.find_all('a', href=True)
        for link in links:
            print("Link:", link['href'])


    except Exception as e:
        print("An error occurred:", str(e))

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Chatbot response
    chatbot_response = chat_with_gpt(f"You: {user_input}\nChatbot:")
    print("Chatbot:", chatbot_response)

    # Check if user wants to scrape a website
    if user_input.lower() == 'scrape':
        website_url = input("Enter the URL of the website: ")
        print("Scraping website...")
        extract_information(website_url)

