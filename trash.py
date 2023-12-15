from translate import Translator
import pyttsx3

def translate_and_speak():
    user_input = input("Enter the text you want to translate: ")

    # Initialize the translator
    translator = Translator(to_lang="hi")  # Change "hi" to "mr" for Marathi

    try:
        # Translate the text
        translated_text = translator.translate(user_input)

        print(f"Translated text: {translated_text}")

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set the translated text to be spoken
        engine.say(translated_text)

        # Start speaking
        engine.runAndWait()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    translate_and_speak()
