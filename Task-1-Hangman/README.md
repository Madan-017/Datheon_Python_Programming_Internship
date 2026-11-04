# Hangman Game – Datheon Python Programming Internship

## 1. Project Overview

Hangman is a terminal-based word guessing game developed using Python. The player attempts to guess a randomly selected hidden English word, one letter at a time, within six incorrect attempts.

The game displays ASCII gallows art that changes whenever the player makes an incorrect guess.

## 2. Features

- Random word selection from an external English word list.
- Hidden word displayed using underscores.
- Maximum of six incorrect attempts.
- ASCII gallows illustration with seven stages.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Displays clear victory and defeat messages.
- Reveals the correct word when the game ends.

## 3. Technologies Used

- Python 3
- Random module
- Pathlib module
- Python standard library

## 4. Project Structure

```text
Task-1-Hangman/
│
├── hangman.py
├── google-10000-english-no-swears.txt
├── README.md
└── requirements.txt
```

## 5. How to Run

1. Install Python 3.
2. Download or clone the project.
3. Keep the English word list in the same folder as `hangman.py`.
4. Open the project folder in VS Code.
5. Open the terminal and execute:

```bash
python hangman.py
```

## 6. How to Play

1. Start the game.
2. Observe the hidden word displayed using underscores.
3. Enter one alphabet letter at a time.
4. Correct guesses reveal matching letters.
5. Incorrect guesses update the ASCII gallows.
6. Avoid making six incorrect guesses.
7. Guess the complete word to win.

## 7. Expected Outcome

The game displays a victory message when the player guesses the complete word correctly.

If the player makes six incorrect guesses, the game displays a defeat message and reveals the hidden word.

## 8. Conclusion

This project demonstrates Python fundamentals, including functions, loops, conditional statements, sets, file handling, random selection, and input validation.

It provides an interactive terminal-based implementation of the classic Hangman word guessing game.

## 9. Internship

**Datheon – Python Programming Internship**
