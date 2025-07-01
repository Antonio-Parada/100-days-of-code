class SimpleSpamClassifier:
    def __init__(self):
        self.spam_keywords = ["free", "win", "prize", "money back", "guarantee", "urgent", "lottery"]

    def classify_message(self, message):
        message_lower = message.lower()
        for keyword in self.spam_keywords:
            if keyword in message_lower:
                return "SPAM", f"Contains keyword: '{keyword}'"
        return "HAM", "No spam keywords found."

if __name__ == "__main__":
    classifier = SimpleSpamClassifier()
    print("--- Simple CLI Spam Classifier (Rule-based) ---")
    print("Type a message to classify (or 'exit' to quit).")

    while True:
        user_message = input("Enter message: ")
        if user_message.lower() == "exit":
            print("Exiting Spam Classifier.")
            break
        
        classification, reason = classifier.classify_message(user_message)
        print(f"Classification: {classification} ({reason})")
