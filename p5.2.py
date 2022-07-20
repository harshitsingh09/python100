# High score
# Find the highest score from a list of student scores

# Taking input from the user
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)

# Finding the highest score using for loop and conditional statements
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

# Displaying output using f-string
print(f"The highest score in the class is {high_score}")