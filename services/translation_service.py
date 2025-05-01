from googletrans import Translator


class TranslationService:
    def __init__(self):
        self.translator = Translator()

    def detect_language(self, text: str) -> str:
        """Detect the language of the given text. example: 'Hola' -> 'es'."""
        result = self.translator.detect(text)
        return result.lang

    def to_english(self, text: str) -> str:
        """Translate text to english if not already in english."""
        lang = self.detect_language(text)
        if lang == 'en':
            return self.translator.translate(text, dest='en').text

        return text

    def to_original_language(self, text: str, target_lang: str) -> str:
        """Translate text to the original language."""
        if target_lang != 'en':
            return self.translator.translate(text, dest=target_lang).text
        return text
