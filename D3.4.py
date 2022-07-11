# Pizza order
# Ask user about the types of topping and fillings, make a bill using the given information.

# Greetings
print('Welcome to the Pizza store!\n')

# Print the menu card to user
print('''Here is the MENU:

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
\n
ORDER:''')

# Take input from user for each category
size = input("What size pizza do you want? S, M, or L (SMALL, MEDIUM OR LARGE)\n")

olive = input("Do you want more Olives? Y or N (YES OR NO)\n")

extraCheese = input("Do you want extra cheese? Y or N (YES OR NO)\n")

# Entering the sequence of IF..ELSE statements
# Creating variable BILL to store sum
bill = 0

# Sequence for pizza size
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('Incorrect value entered!')

# Sequence for Olives
if olive == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# Sequence for Extra cheese
if extraCheese == 'Y':
    bill += 1

# Displaying output to the user
print(f'The total bill is = {bill}')