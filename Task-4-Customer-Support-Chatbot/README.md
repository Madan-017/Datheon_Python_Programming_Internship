
# Task 4 - Rule-Based Customer Support Chatbot

## 1. Project Overview

This project is a rule-based customer support chatbot developed using Python. It interacts with users, identifies their questions using keywords and regular expressions, and provides suitable responses from a predefined FAQ dataset.

## 2. Objectives

- Develop an interactive customer support chatbot.
- Identify user intent using keywords and regular expressions.
- Provide answers to frequently asked questions.
- Handle greetings and unknown questions.
- Support exit commands for ending conversations.

## 3. Features

- **Greeting Detection:** Recognizes greetings such as hello, hi, and good morning.
- **Business Hours FAQ:** Provides information about working days and operating hours.
- **Project Submission FAQ:** Explains how to submit internship projects.
- **Certificate FAQ:** Provides information about certificate processing.
- **Fallback Handling:** Gives a helpful response when a question is not recognized.
- **Exit Commands:** Supports bye, exit, and quit.
- **Input Processing:** Converts user input to lowercase and removes extra spaces.
- **Error Handling:** Handles missing or invalid JSON files.

## 4. Technologies Used

- Python 3
- Regular Expressions (`re`)
- JSON (`json`)
- pathlib (`pathlib`)

## 5. Project Structure

```text
Task-4-Customer-Support-Chatbot/
│
├── chatbot.py
├── sample_faq.json
└── README.md
```

## 6. How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python chatbot.py
```

5. Enter your questions when the chatbot displays the `You:` prompt.

## 7. Sample Questions

| User Input | Expected Response |
|---|---|
| hello | Greeting message |
| What are your hours of operation? | Business hours |
| How do I submit my internship project? | Project submission instructions |
| When will I receive my certificate? | Certificate processing information |
| What is the weather today? | Fallback response |
| bye | Exit message |

## 8. Advantages

- Simple and easy to use.
- Provides quick responses to common questions.
- Does not require an internet connection.
- Uses a separate JSON file to store FAQ information.
- Easy to maintain and extend with additional FAQ patterns.

## 9. Limitations

- Uses predefined keywords and regular expressions.
- Cannot understand complex questions outside its programmed patterns.
- Does not use machine learning or natural language processing.
- Responses are limited to the available FAQ dataset.

## 10. Conclusion

The Rule-Based Customer Support Chatbot demonstrates how Python can be used to build a simple interactive support system. By combining keyword matching, regular expressions, JSON data, and fallback handling, the chatbot can identify common user questions and provide relevant responses.
