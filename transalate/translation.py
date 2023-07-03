import requests

# Sunbird AI API endpoint
url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk'  # Replace sunbird ai API key

# Helper function to translate text
def translate_text(source_language, target_language, text):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # this creates a dictionary called payloads containing the data to be sent in the API requests
    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
    # this sends POST requests
    if response.status_code == 200:
        translated_text = response.json()["text"]
        print("Translated text:", translated_text)
        # this shows where the error is
    elif response.status_code ==422:
        error_message = response.json()["detail"][0]["msg"]
        print("please choose one language:")
    else:
        print("Error:", response.status_code, response.text)

# Prompt the user for source language
source_language = input("Please choose the source language (English, Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")

# Prompt the user for target language if the source language is English, otherwise set English as the target language
if source_language.lower() == "english":
    target_language = input("Please choose the target language (Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")
else:
    target_language = "English"

# Prompt the user for text to translate
text = input("Enter the text to translate: ")

# Translate the input text into the target language
translate_text(source_language, target_language, text)
