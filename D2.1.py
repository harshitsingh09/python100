# DIGIT ADDITION
print("Welcome to the digit addition calculator")

# takes input from user
num = input("Enter a two digit interger!\n")

# find type of variable num
#print(type(num))

# display first digit
#print(num[0])

# display second digit
#print(num[1])

# Adding both values and storing in variable num
# Converting datatype of num values from string to integer
sum = int(num[0]) + int(num[1])

# displaying sum output
print("The sum of digits in 2 digit integer =", sum)