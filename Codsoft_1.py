import re

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase to make matching case-insensitive

    if re.search(r"\bhello\b|\bhi\b", user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r"\bhow are you\b", user_input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r"\byour name\b", user_input):
        return "I am a simple chatbot created to assist you."
    elif re.search(r"\byou can do\b|\byou can provide\b", user_input):
        return "I can answer to some of your queries based on predefined rules."
    elif re.search(r"\bbye\b|\bgoodbye\b", user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


print("Welcome to the simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if re.search(r"\bbye\b|\bgoodbye\b", user_input.lower()):
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")

