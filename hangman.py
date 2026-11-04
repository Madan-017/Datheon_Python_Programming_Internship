
import random
from pathlib import Path

# ==========================================
# DATHEON INTERNSHIP - TASK 1
# HANGMAN WORD GUESSING GAME
# ==========================================

MAX_ATTEMPTS = 6

# Locate the external word list
WORD_FILE = Path(__file__).parent / "google-10000-english-no-swears.txt"

# ASCII gallows stages: initial + 6 incorrect guesses
HANGMAN_STAGES = [
    """
       _______
      |/      |
      |
      |
      |
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |
      |
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |       |
      |
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |      /|
      |
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |      /|\\
      |
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |      /|\\
      |      /
      |
    __|________
    """,
    """
       _______
      |/      |
      |       O
      |      /|\\
      |      / \\
      |
    __|________
    """
]


def load_words():
    """Read and prepare words from the external text file."""

    if not WORD_FILE.exists():
        raise FileNotFoundError(
            "Word list file is missing. Keep it beside hangman.py."
        )

    with open(WORD_FILE, "r", encoding="utf-8") as file:
        words = [
            line.strip().lower()
            for line in file
            if line.strip().isalpha()
            and 4 <= len(line.strip()) <= 12
        ]

    if not words:
        raise ValueError("No valid words found in the word list.")

    return words


def display_game(secret_word, guessed_letters, mistakes):
    """Display the current gallows and guessing progress."""

    print(HANGMAN_STAGES[mistakes])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Hidden word:", masked_word)

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    print("Incorrect attempts remaining:", MAX_ATTEMPTS - mistakes)


def play_game():
    """Main function to run the Hangman game."""

    words = load_words()
    secret_word = random.choice(words)

    guessed_letters = set()
    mistakes = 0

    print("\n======================================")
    print("         WELCOME TO HANGMAN")
    print("======================================")
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect attempts.")
    print("Enter only one alphabet letter per turn.\n")

    while mistakes < MAX_ATTEMPTS:

        display_game(secret_word, guessed_letters, mistakes)

        # Check whether the player has guessed the entire word
        if all(letter in guessed_letters for letter in secret_word):
            print("\n======================================")
            print("       CONGRATULATIONS! YOU WON!")
            print("======================================")
            print("The correct word was:", secret_word)
            return

        guess = input("\nEnter your guess: ").strip().lower()

        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter one alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        # Check whether the guessed letter is in the secret word
        if guess in secret_word:
            print("Correct guess!")
        else:
            mistakes += 1
            print("Wrong guess! One attempt deducted.")

    # Display the final gallows after six incorrect guesses
    display_game(secret_word, guessed_letters, mistakes)

    print("\n======================================")
    print("             GAME OVER!")
    print("======================================")
    print("You have used all 6 incorrect attempts.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    try:
        play_game()
    except (FileNotFoundError, ValueError) as error:
        print("\nError:", error)
