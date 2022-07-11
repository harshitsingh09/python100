# Leap year
# Create a test for a leap year

# Greetings
print('Welcome to the leap year test!')

# Taking input year to test on
year = int(input('Enter the year you want to test out:\n'))

# Leap year test using IF..ELSE statements
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('This is a Leap year!\n')
        else:
            print('Not a leap year.')
    else:
        print('This is a leap year!')
else:
    print('Not a leap year.')
# Display output using print statement