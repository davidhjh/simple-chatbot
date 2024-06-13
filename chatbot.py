import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I am doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

# Default reflections for input matching
chat = Chat(pairs, reflections)


def chatbot():
    print("Hi, I'm a chatbot! Type 'quit' to exit.")
    chat.converse()

if __name__ == "__main__":
    chatbot()
