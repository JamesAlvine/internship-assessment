import requests
from colorama import Fore, Style
from termcolor import colored

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk"

def translate_text(source_lang, target_lang, text):
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "source_language": source_lang,
        "target_language": target_lang,
        "text": text
    }
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
    if response.status_code == 200:
        translated_text = response.json()["text"]
        return translated_text
    else:
        return "Translation Error"

def choose_target_language():
    print("(your program): Please choose the target language: (one of Luganda, Runyankole, Ateso, Lugbara, or Acholi)")
    target_lang = input("(the user): ")
    return target_lang

def get_user_input(source_lang):
    print("(your program): Enter the text to translate:")
    text = input("(the user): ")
    target_lang = "English" if source_lang != "English" else choose_target_language()
    translated_text = translate_text(source_lang, target_lang, text)
    translated_text = colored(translated_text, "green")
    print("(your program):", translated_text)

def main():
    print("(your program): Please choose the source language:")
    source_lang = input("(the user): ")
    get_user_input(source_lang)

if __name__ == "__main__":
    main()
