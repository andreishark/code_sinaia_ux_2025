from flask import Flask, request
import grpc
from chatbot.chatbot import get_response
from models.chatbot_response import ChatbotResponse

app = Flask(__name__)


@app.route("/")
def hello_world():
    query = request.args.get("query")
    response = get_response(query)

    if response is None:
        response = "An error has occured"
    return ChatbotResponse(response).__dict__


if __name__ == "__main__":
    app.run()
