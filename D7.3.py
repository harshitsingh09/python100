# Hangman (Challenge 2)
# Checking if the player Won

# Selecting a random word out of the three using the random module
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Displaying the chosen word
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
display = []

# For each letter in the chosen_word, add a "_" to 'display'
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# Take input from the user
guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word
# If the letter at that position matches 'guess' then reveal that letter in the display at that position
for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

# Print 'display' and you should see the guessed letter in the correct position
print(display)