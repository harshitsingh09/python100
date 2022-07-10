# Odd or Even number
# Code to tell whether a number is even or odd

# Greetings
print('Welcome to the odd-even tester!\n')

# Taking input from the user
num = int(input('Enter the value to test:\n'))

# Using modulus operator we find if value is even or not
# Using IF..ELSE statements to print whether value is odd or even.
if num % 2 == 0:
    print(f'Number {num} is EVEN!')
else:
    print(f'Number {num} is ODD!')

# ..print statement used to display output
#ll