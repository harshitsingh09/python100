# Using the Random module

# Importing the random module
import random

# Entering seed value
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Entering a random integer into random_side variable
random_side = random.randint(0,1)

# Using conditional statements to print desired output
if random_side == 1:
    print('Heads')
else:
    print('Tails')