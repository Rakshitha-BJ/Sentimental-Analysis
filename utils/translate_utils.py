from langdetect import detect
from deep_translator import GoogleTranslator

def translate_to_english(text):
    try:
        lang = detect(text)
        if lang != 'en':
            return GoogleTranslator(source=lang, target='en').translate(text)
        return text
    except Exception:
        return text
