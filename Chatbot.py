def chatbot():
    print("Hello! I'm your friendly chatbot. How can I assist you today?")
    print("Type 'bye' or 'exit' to end the conversation.")

    while True:
        user_input=input("you: ").lower()

        if "Hello" in user_input or "Hi" in user_input:
            print("chatbot: Hello! How can I help you today?")

        elif "bye" in user_input or "exit" in user_input:
            print("chatbot: Goodbye! Have a great day!")
            break
        else:
            print("chatbot: I'm not sure I understand. Could you please rephrase that?")
            