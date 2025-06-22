def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hi there! How can I help you?")
        elif 'how are you' in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great! 😊")
        elif 'your name' in user_input:
            print("Bot: I'm ChatBuddy, your Python chatbot.")
        elif 'bye' in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: I'm not sure I understand. Can you rephrase that?")

chatbot()
