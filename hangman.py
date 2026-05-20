import random
words = ["Legs", "Nose", "Feet", "Toes", "Hands"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6
hangman_stages = [
    """
-----
|   |
|   
|   
|   
|   
=========
""",
    """
-----
|   |
|   O
|   
|   
|   
=========
""",
    """
-----
|   |
|   O
|   |
|   
|   
=========
""",
    """
-----
|   |
|   O
|  /|
|   
|   
=========
""",
    """
-----
|   |
|   O
|  /|\\
|   
|   
=========
""",
    """
-----
|   |
|   O
|  /|\\
|  /
|   
=========
""",
    """
-----
|   |
|   O
|  /|\\
|  / \\
|   
=========
"""
]

print("Welcome to Hangman!")
while wrong_guesses < max_attempts:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])
        print(f"Wrong guess! Attempts left: {max_attempts - wrong_guesses}")
if wrong_guesses == max_attempts:
    print("Game Over!")
    print("The correct word was:", word)