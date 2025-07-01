import random
import time

class TypingPractice:
    def __init__(self):
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Never underestimate the power of a good book.",
            "Practice makes perfect, especially in coding.",
            "The early bird catches the worm, but the second mouse gets the cheese.",
            "Innovation distinguishes between a leader and a follower."
        ]

    def calculate_wpm(self, text, elapsed_time):
        words = len(text.split())
        minutes = elapsed_time / 60
        wpm = words / minutes
        return round(wpm)

    def calculate_accuracy(self, original_text, typed_text):
        correct_chars = 0
        min_len = min(len(original_text), len(typed_text))
        for i in range(min_len):
            if original_text[i] == typed_text[i]:
                correct_chars += 1
        accuracy = (correct_chars / len(original_text)) * 100
        return round(accuracy, 2)

    def start_practice(self):
        sentence = random.choice(self.sentences)
        print("\nType this sentence:")
        print("------------------------------------------------------------------")
        print(sentence)
        print("------------------------------------------------------------------")

        input("Press Enter when you are ready to start...")
        start_time = time.time()

        typed_input = input("Start typing: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        wpm = self.calculate_wpm(typed_input, elapsed_time)
        accuracy = self.calculate_accuracy(sentence, typed_input)

        print(f"\nTime taken: {elapsed_time:.2f} seconds")
        print(f"Words Per Minute (WPM): {wpm}")
        print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    practice = TypingPractice()
    print("--- CLI Typing Practice App ---")
    
    while True:
        choice = input("\nType 'start' to begin practice or 'exit' to quit: ").lower()
        if choice == "start":
            practice.start_practice()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")