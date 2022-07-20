# Hangman (Challenge 2)
# Test each letter in a word against the user entered letter in a list

# Generating list of words
wordList = ["ardvark", "baboon", "camel"]

# Selecting on word from given list
import random
word = random.choice(wordList)
print(f'\nPsst! The chosen word is {word}\n')

# Converting the word into a list
wordList = list(word)
#print(wordList)

# Entering dashes into the list (same no. of letters as in the word)
blank = []
for letter in word:
    blank.append('_')
print(blank)

# Taking a letter input from user
guess = str(input('\nEnter a letter!\n-> ')).lower()

# Testing each letter of word against the user entered letter
for letter in range(len(word)):
    if word[letter] == guess:
        blank[letter] == guess
print(blank)