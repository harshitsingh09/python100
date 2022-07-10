# Life in Weeks
# Program to calculate the approximate time remaining for a person until natural death, assuming maximum age as 90

# Take input from user
age = input('Enter your age:\n')

# Convert age to integer
age = int(age)

# Calculating years remaining
yearsRemain = 90 - age

# Caluclating days remaining
daysRemain = yearsRemain*365

# Calculating weeks remaining
weeksRemain = yearsRemain*52

#Calculating months remaining
monthsRemain = yearsRemain*12

# Output statement using F-strings
output = f"You have about {daysRemain} days, {weeksRemain} weeks, {monthsRemain} months and {yearsRemain} years left"

# Display output to user
print(output)