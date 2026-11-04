
import json
import re
from pathlib import Path


def load_faq_data():
    """Load greetings and FAQ answers from the JSON file."""
    file_path = Path(__file__).with_name("sample_faq.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: sample_faq.json was not found.")
        return None

    except json.JSONDecodeError:
        print("Error: sample_faq.json contains invalid JSON.")
        return None


def normalize_input(user_input):
    """Convert input to lowercase and remove extra spaces."""
    return re.sub(r"\s+", " ", user_input.lower().strip())


def get_response(user_input, faq_data):
    """Identify the user's intent and return a suitable response."""
    message = normalize_input(user_input)

    # Exit commands
    if re.fullmatch(r"(bye|exit|quit)[!. ]*", message):
        return "Goodbye! Thank you for contacting customer support.", True

    # Greeting detection
    for greeting in faq_data["greetings"]:
        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, message):
            return (
                "Hello! Welcome to customer support.\n "
                "1)You can ask me about business hours\n "
                "2)internship project submission\n  3) certificates.\n",
                False
            )

    # FAQ keyword patterns
    faq_patterns = [
        r"\b(hours?|timings?|operation|open|closing|working days?)\b",
        r"\b(submit|submission|upload|project|github|repository|student workspace)\b",
        r"\b(certificate|certification|code review)\b"
    ]

    for pattern, faq in zip(faq_patterns, faq_data["faqs"]):
        if re.search(pattern, message):
            return faq["answer"], False

    # Fallback response
    return (
        "Sorry, I couldn't understand your question. "
        "Please ask about business hours, project submission, "
        "or certificates.",
        False
    )


def start_chatbot():
    """Start the interactive customer support chatbot."""
    faq_data = load_faq_data()

    if faq_data is None:
        return

    print("\n======================================")
    print("   CUSTOMER SUPPORT CHATBOT")
    print("======================================")
    print("Hello! How can I help you today?")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please enter a message.\n")
            continue

        response, should_exit = get_response(user_input, faq_data)

        print("Bot:", response, "\n")

        if should_exit:
            break


if __name__ == "__main__":
    start_chatbot()
