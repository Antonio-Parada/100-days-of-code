class SimpleTranslator:
    def __init__(self):
        self.dictionary = {
            "hello": "bonjour",
            "world": "monde",
            "cat": "chat",
            "dog": "chien",
            "house": "maison",
            "thank you": "merci"
        }

    def translate_word(self, word):
        return self.dictionary.get(word.lower(), word)

    def translate_sentence(self, sentence):
        words = sentence.split()
        translated_words = [self.translate_word(word) for word in words]
        return " ".join(translated_words)

if __name__ == "__main__":
    translator = SimpleTranslator()
    print("--- Simple CLI Machine Translator (Rule-based) ---")
    print("Type a sentence to translate (English to French, very limited vocabulary).")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter English sentence: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        translated_sentence = translator.translate_sentence(user_input)
        print(f"Translated: {translated_sentence}")
