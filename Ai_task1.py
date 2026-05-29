print("Welcome to the Rule-Based AI Chatbot! (Type 'bye' or 'exit' to quit)")

responses = {
    'hello': 'Hi there!',
    'hi': 'Hello! How can I help you?',
    'how are you': "I'm doing well, thanks for asking!",
    'help': 'I can answer basic questions about myself. Try saying "hello", "how are you", or ask my name.',
    'what is your name': "I'm a simple rule-based chatbot. You can call me RuleBot.",
    'who are you': "I'm RuleBot—your friendly AI assistant!",
    'bye': 'Goodbye! Have a great day!',
    'goodbye': 'See you soon!',
    'what can you do': 'I can answer simple rule-based questions. Try greetings, asking my name, or request help!'
}

EXIT_COMMANDS = ['exit', 'quit', 'bye', 'goodbye']

while True:
    user_input = input("You: ")
    cleaned_input = user_input.lower().strip()
    if cleaned_input in EXIT_COMMANDS:
        print("Chatbot: Goodbye! Chat ended.")
        break
    reply = responses.get(cleaned_input, "I do not understand. Can you rephrase?")
    print("Chatbot:", reply)