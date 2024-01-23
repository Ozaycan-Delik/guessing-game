# Import the random module
import random

# Define a list of words to choose from
words = ["apple", "banana", "cherry", "dragon", "elephant", "mango", "grape", "fruit", "ball", "sea"]

# Pick a random word from the list
word = random.choice(words)

# Initialize the number of guesses
guesses = 0

# Initialize the list of letters that have been guessed
guessed = []

# Prompt the user to guess the word
print("I'm thinking of a word with", len(word), "letters. Can you guess it?")

# Loop until the user guesses the word or runs out of guesses
while guesses < 6:
    # Display the word with dashes for the letters that have not been guessed
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "-"
    print(display)

    # Get the user's input
    guess = input("Enter a letter or the whole word: ")

    # Check if the guess is correct
    if guess == word:
        # Congratulate the user and end the game
        print("You got it! The word was", word)
        break
    # Check if the guess is a single letter
    elif len(guess) == 1:
        # Check if the letter has already been guessed
        if guess in guessed:
            print("You already guessed that letter. Try again.")
        # Check if the letter is in the word
        elif guess in word:
            print("Good guess! That letter is in the word.")
            # Add the letter to the list of guessed letters
            guessed.append(guess)
        # If the letter is not in the word
        else:
            print("Sorry, that letter is not in the word.")
            # Increment the number of guesses
            guesses += 1
    # If the guess is not a single letter or the whole word
    else:
        print("Invalid guess. Please enter a single letter or the whole word.")

# If the user runs out of guesses, reveal the word and end the game
if guesses == 6:
    print("Sorry, you ran out of guesses. The word was", word)
