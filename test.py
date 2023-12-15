import indic_transliteration
from translate import Translator
import pyttsx3

def transliterate_hindi_to_english(hindi_text):
    # Transliterate Hindi text to English using Indic Transliteration library
    english_text = indic_transliteration.transliterate(hindi_text, indic_transliteration.ISO, indic_transliteration.ITRANS)
    return english_text

def speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the text to be spoken
    engine.say(text)

    # Start speaking
    engine.runAndWait()

def translate_transliterate_and_speak():
    user_input = input("Enter the text you want to translate and transliterate: ")

    try:
        # Translate the input text to Hindi
        translator = Translator(to_lang="hi")
        translated_text = translator.translate(user_input)

        print(f"Translated text (Hindi): {translated_text}")

        # Transliterate the translated text from Hindi to English
        english_text = transliterate_hindi_to_english(translated_text)

        print(f"Transliterated text (English): {english_text}")

        # Speak the transliterated text
        speak_text(english_text)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    translate_transliterate_and_speak()
