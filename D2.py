# Tip calculator
# Allow the user to enter a percentage of tip that each customers can give.

# Greetings
print('Welcome to the tip calculator!\n')

# Taking input of total bill value
bill = float(input('What is the total bill?\nRs.'))

# Ask for the total percentage of tip user would like to give
percent = float(input('What is the bill percentage tip you would like to give?\n'))

# Ask how many people are paying
people = float(input('How many people to split bill?\n'))

# ...Converting all values to float to get a more accurate/precise result

# Calculate the tip percentage of total bill
tip = (bill * (percent/100))
tip = float(tip)

# Total bill with tip included
total = float(bill + tip)

# Spliting the bill
eachPerson = str(float(total/people))

# Displaying output to user
output = "Each person should pay: Rs." + eachPerson
print(output)