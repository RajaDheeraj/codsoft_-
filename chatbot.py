import re


def chatbot():
    print("Chatbot: Hi! I'm your rule-based assistant. How can I help you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Predefined rules and responses
        if re.search(r'hi|hello|hey', user_input):
            print("Chatbot: Hello! How can I assist you today?")
        elif re.search(r'weather|temperature', user_input):
            print("Chatbot: I can't give live weather updates, but you can try a weather app!")
        elif re.search(r'time|date', user_input):
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
        elif re.search(r'help|support', user_input):
            print("Chatbot: Sure! I'm here to help. Please let me know your query.")
        elif re.search(r'your name|who are you', user_input):
            print("Chatbot: I'm a simple rule-based chatbot created for learning purposes!")
        elif re.search(r'thank you|thanks', user_input):
            print("Chatbot: You're welcome! Is there anything else I can help you with?")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase your question?")


# Run the chatbot
if __name__ == "__main__":
    chatbot()
