def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I am a bot, so I don't have feelings, but I'm ready to assist you!"
    elif "your name" in user_input:
        return "I am a simple chatbot created to help you."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I cannot provide real-time weather information."
    else:
        return "I'm sorry, I don't understand that. Can you rephrase?"

if __name__ == "__main__":
    print("Simple Chatbot (Type 'bye' to exit)")
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_message)
        print(f"Bot: {response}")
