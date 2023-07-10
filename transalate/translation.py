import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Sunbird AI API endpoint
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
api_key = os.getenv('API_KEY')

# List of target languages
target_languages = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

# Helper function to translate text
def translate_text(source_language, target_language, text):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        return translated_text
    elif response.status_code == 422:
        error_message = response.json()["detail"][0]["msg"]
        raise ValueError(f"Translation Error: {error_message}")
    else:
        raise ValueError(f"Translation Error: {response.status_code} - {response.text}")

def get_language_choice(prompt, options):
    while True:
        print(prompt)
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
        choice = input("Enter your choice number: ")
        if choice.isdigit() and int(choice) in range(1, len(options) + 1):
            return options[int(choice) - 1]

def main():
    # Prompt the user for source language
    source_language = input("Please enter the source language: ")

    # Prompt the user to choose the target language
    target_language = get_language_choice("Please choose the target language:", target_languages)

    # Prompt the user for text to translate
    text = input("Enter the text to translate: ")

    # Translate the input text into the target language
    try:
        translated_text = translate_text(source_language, target_language, text)
        print(f"Translated text: {translated_text}")
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
