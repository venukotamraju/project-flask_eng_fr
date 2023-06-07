from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    '''This function converts
        English text to French'''
    translator=MyMemoryTranslator(source='en',target='fr')
    french_text=translator.translate(english_text)
    return french_text
def french_to_english(french_text):
    '''This function translates french to english'''
    translator=MyMemoryTranslator(source='fr',target='en')
    english_text=translator.translate(french_text)
    return english_text
