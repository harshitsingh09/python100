# Treasure Map
# Program to mark an X at any given co-ordinate in the matrix

# Preparing the matrix to be worked upon
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Creating a multi-list 'map'
map = [row1, row2, row3]

# Displaying our map
print(f"{row1}\n{row2}\n{row3}")

# Asking for double digit integer from user
position = input("Where do you want to put the treasure? ")

# Setting up the variables
x = int(position[0])-1
y = int(position[1])-1

# Referencing the variable to change to 'X'
map[y][x] = "X"

# Printing the final Map!
print(f"{row1}\n{row2}\n{row3}")
