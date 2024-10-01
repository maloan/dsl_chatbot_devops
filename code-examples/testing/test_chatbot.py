import pytest
from chatbot import Chatbot

def test_get_known_response():
    bot = Chatbot()
    response = bot.get_response("admission")
    assert response == "Admission starts in September."

def test_get_unknown_response():
    bot = Chatbot()
    response = bot.get_response("unknown query")
    assert response == "Sorry, I don't have an answer for that."

def get_response(question):
    responses = {
        "Where is the library?": "The library is on the main campus.",
        "What are the admission requirements?": "A high school diploma."
    }
    return responses.get(question, "I don't know.")

def test_get_response():
    assert get_response("Where is the library?") == "The library is on the main campus."
    assert get_response("Unknown question") == "I don't know."

