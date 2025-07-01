import random

def process_message(message):
    message_lower = message.lower()

    if message_lower == "/start":
        return "Hello! I am a simple messenger bot. You can ask me to flip a coin, roll a dice, or tell you a joke."
    elif message_lower == "/flipcoin":
        return random.choice(["Heads", "Tails"])
    elif message_lower.startswith("/rolldice"):
        try:
            parts = message_lower.split()
            if len(parts) == 2:
                num_dice = int(parts[1])
                if num_dice > 0:
                    rolls = [random.randint(1, 6) for _ in range(num_dice)]
                    return f"You rolled: {', '.join(map(str, rolls))}. Total: {sum(rolls)}"
                else:
                    return "Please specify a positive number of dice to roll."
            else:
                return "Usage: /rolldice <number_of_dice>"
        except ValueError:
            return "Invalid number of dice. Usage: /rolldice <number_of_dice>"
    elif "joke" in message_lower:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who was afraid of negative numbers? He'd stop at nothing to avoid them.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        return random.choice(jokes)
    elif "news" in message_lower:
        return "I'm sorry, I cannot fetch real-time news in this basic version."
    else:
        return "I'm not sure how to respond to that. Try /start for commands."

if __name__ == "__main__":
    print("Generic Messenger Bot (CLI Simulation)")
    print("Type your message (e.g., /flipcoin, /rolldice 2, tell me a joke):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = process_message(user_input)
        print(f"Bot: {response}")
