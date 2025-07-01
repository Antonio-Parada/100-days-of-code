from textblob import TextBlob

class GrammarChecker:
    def __init__(self):
        pass

    def spell_check(self, text):
        blob = TextBlob(text)
        corrected_text = str(blob.correct())
        if corrected_text != text:
            print(f"Original: {text}")
            print(f"Corrected: {corrected_text}")
            return corrected_text
        else:
            print("No spelling errors found.")
            return text

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity

        mood = "neutral"
        if sentiment_polarity > 0.1:
            mood = "positive"
        elif sentiment_polarity < -0.1:
            mood = "negative"
        
        print(f"\nSentiment Analysis for: '{text}'")
        print(f"  Polarity (emotion): {sentiment_polarity:.2f} (closer to 1 is positive, -1 is negative)")
        print(f"  Subjectivity (opinion vs. fact): {sentiment_subjectivity:.2f} (closer to 1 is subjective, 0 is objective)")
        print(f"  Inferred Mood: {mood}")
        return mood

if __name__ == "__main__":
    checker = GrammarChecker()
    print("--- Simple CLI Grammar Checker (requires textblob: pip install textblob, python -m textblob.download_corpora) ---")
    
    while True:
        print("\nCommands: spellcheck <text>, sentiment <text>, exit")
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "spellcheck":
            if len(command_input) == 2:
                checker.spell_check(command_input[1])
            else:
                print("Usage: spellcheck <text>")
        elif cmd == "sentiment":
            if len(command_input) == 2:
                checker.analyze_sentiment(command_input[1])
            else:
                print("Usage: sentiment <text>")
        elif cmd == "exit":
            print("Exiting Grammar Checker.")
            break
        else:
            print("Unknown command.")