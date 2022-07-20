# Average height
# Program to find the average height from a list of students

# Taking input from user
# Enter values with space in between values
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#print(student_heights)

# Calculating the total Height sum
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)

# Calculating the total number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
#print(number_of_students)

# Calculating the average of Heights
average = round(total_height/number_of_students)

#Displaying the output
print(average)