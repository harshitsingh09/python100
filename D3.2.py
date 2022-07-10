# BMI range calculator
# This calculator calculates the range in which your BMI falls

# Greeting
print('Welcome to your BMI range Calculator!')

# Taking height input
H = float(input("Enter your height:\n"))

# Taking weight input
W = float(input("Enter your weight:\n"))

# Calculating their BMI using formula
bmi = float(W/(H**2))

# Find the range in which the BMI is in.
# Using IF..ELSE statements
if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight!')
elif 25 > bmi > 18.5:
    print(f'Your BMI is {bmi}, you are fit!')
elif 30 > bmi > 25:
    print(f'Your BMI is {bmi}, you are overweight!')
elif 35 > bmi > 30:
    print(f'Your BMI is {bmi}, you are obese!')
else:
    print(f'Your BMI is {bmi}, you will die sooner!')

# Display the range to user