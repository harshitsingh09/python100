# TRUE LOVE test

# Calculate the percentage of love using the children's algorithm
# Link for concept [https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love?utm_source=dynamic&utm_campaign=bfsharecopy]

# Greetings
print('Welcome to your T-R-U-E L-O-V-E calculator')

# Taking names as input
name1 = input('Enter the name of first person:\n')
name2 = input('Enter the name of the second person:\n')

# Joining the names to simplify character search
name = name1 + name2
name = name.lower().strip()

# Searching total count of individual characters using .count() function
T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")
L = name.count("l")
O = name.count("o")
V = name.count("v")

# Displaying the tally of each character
# Finding sum of TRUE and LOVE individually
print(f'T occurs {T} times')
print(f'R occurs {R} times')
print(f'U occurs {U} times')
print(f'E occurs {E} times')
sumTRUE = T + R + U + E
print(f'Total = {sumTRUE}')
print(f'L occurs {L} times')
print(f'O occurs {O} times')
print(f'V occurs {V} times')
print(f'E occurs {E} times')
sumLOVE = L + O + V + E
print(f'Total = {sumLOVE}')

# Finding the total love score percent
score = sumTRUE*10 + sumLOVE

# Displaying the final result
#print(f'Both of your Love score is {score}%')

# Calculating the love range using IF..ELIF..ELSE statements
# Displaying output
if score > 90 or score < 10:
    print(f'Your score is {score}, you go together like Coke and Mentos!')
elif score > 40 and score < 60:
    print(f'Your score is {score}%, you both are alright together.')
else:
    print(f'Your TRUE LOVE score is {score}.')