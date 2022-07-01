# BMI calculator
print("Welcome to your BMI calculator!")

# Takes input interger in variable W
W = int(input("Enter your weight:\n"))

# Takes input integer in variable H
H = int(input("Enter your height:\n"))

# calculates the BMI of person using formula [BMI = W/(H^2)]
bmi = W/(H**2)

# display the BMI value as output
print(bmi)
##