import re

# Define patterns and corresponding responses
patterns_and_responses = {
    r"hi|hello|hey": "Hello! How can I assist you?",
    r"how are you|how's it going": "It's a great plesure!",
    r"bye|goodbye": "Goodbye! Have a great day!",
}

def respond_to_user_input(user_input):
    for pattern, response in patterns_and_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = respond_to_user_input(user_input)
    print("Chatbot:", response)
