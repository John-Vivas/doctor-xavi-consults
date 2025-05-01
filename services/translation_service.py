from langdetect import detect
from deep_translator import GoogleTranslator


class TranslationService:
    def __init__(self):
        self.translator = GoogleTranslator()

    def detect_language(self, text: str) -> str:
        """Detect the language of the given text using langdetect."""
        return detect(text)  # Usando langdetect para detectar el idioma

    def to_english(self, text: str) -> str:
        """Translate text to english if not already in english."""
        lang = self.detect_language(text)
        if lang == 'en':
            return text
        return self.translator.translate(text, source='auto', target='en')

    def to_original_language(self, text: str, target_lang: str) -> str:
        """Translate text to the original language."""
        if target_lang != 'en':
            return self.translator.translate(text, source='auto', target=target_lang)
        return text
