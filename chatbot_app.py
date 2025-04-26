from chatbot.chatbot import get_response

if __name__ == "__main__":
    while True:
        print("Bot: " + get_response(input("You: ")))
