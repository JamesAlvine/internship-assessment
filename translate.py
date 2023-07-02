from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    # Initialize the translation client with your API key
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk"  # sunbird.ai API key
    client = translate.Client(api_key)

    # Translate the text
    result = client.translate(text, target_language=target_language)

    # Return the translated text
    return result["translatedText"]

if __name__ == "__main__":
    # Mapping of target languages
    target_languages = {
        "Luganda": "lg",
        "Runyankole": "rn",
        "Ateso": "teo",
        "Lugbara": "lgg",
        "Acholi": "ach"
    }

    # Prompt user for source language
    source_language = "English"  # Default source language

    # Prompt user for target language
    target_language = input("Please choose the target language: (one of Luganda, Runyankole, Ateso, Lugbara or Acholi): ")

    # Validate target language
    while target_language not in target_languages:
        target_language = input("Invalid target language. Please choose one of Luganda, Runyankole, Ateso, Lugbara or Acholi: ")

    target_language_code = target_languages[target_language]

    # Prompt user for text to translate
    text = input("Enter the text to translate: ")

    # Perform translation
    translated_text = translate_text(text, target_language_code)

    # Print the result
    print(f"{translated_text}")
