# Hangman (Challenge 1)
# Test each letter in a word against the user entered letter

# Generating list of words
wordList = ["ardvark", "baboon", "camel"]

# Selecting on word from given list
import random
word = random.choice(wordList)

# Take a letter input from user
guess = str(input('Enter a letter!\n-> ')).lower()

# Test each letter of word against the user entered letter
for letter in word:
    if letter == guess:
        print(guess)
    else:
        print('x')