# Person to pay

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ran = random.randit(0, len(names)-1)
name = names[ran]
print(f"{ran} is going to pay today!")