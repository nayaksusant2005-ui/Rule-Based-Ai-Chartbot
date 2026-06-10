# Rule-Based AI Chatbot
# DecodeLabs Project 1

print("=" * 50)
print("🤖 Welcome to DecodeBot!")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)

responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! How can I help you?",
    "good morning": "Good Morning!",
    "good night": "Good Night!",
    "python": "Python is a programming language.",
    "ai": "Artificial Intelligence enables machines to think and learn.",
    "who made you": "I was created for DecodeLabs Project 1.",
    "hey": "Hey! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking. 😊",
    "your name": "My name is DecodeBot.",
    "who are you": "I am a Rule-Based AI Chatbot.",
    "help": "I can answer simple predefined questions.",
    "thanks": "You're welcome! 😊",
    "thank you": "Glad I could help!",
    "good morning": "Good Morning! Have a productive day. ☀️",
    "good afternoon": "Good Afternoon! 😊",
    "good evening": "Good Evening! 🌇",
    "good night": "Good Night! Sweet Dreams. 🌙",
    "python": "Python is a popular programming language used in AI and Web Development.",
    "ai": "Artificial Intelligence enables machines to simulate human intelligence.",
    "machine learning": "Machine Learning is a branch of AI that learns from data.",
    "who made you": "I was created for DecodeLabs Project 1.",
    "what can you do": "I can respond to predefined questions and demonstrate rule-based AI.",
    "bye": "Goodbye! Have a great day! 👋"
}

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Please try another question."
    )

    print("Bot:", response)