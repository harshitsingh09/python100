# Fizz Buzz Game
'''
Program for Fizz-Buzz.
From 1 to 100:
If divisible by 3, say 'Fizz';
If any number is divisible by 5, say 'Buzz';
If any number is divisible by 3 and 5, say 'FizzBuzz';
print all the other numbers regularly
'''

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)