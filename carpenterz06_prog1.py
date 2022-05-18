"""
Author:  Zac Carpenter
Course:  CSC 121
Assignment:  Lesson 06: Lab - Part 1 Rewrite For Loop as While Loop
Purpose:  carpenterz06_prog1.py
	This program loops through the user
    input age and prints the question
    Are you __. The blank representing an
    age number.
"""

"""
age = input("How old are you?")
age = int(age)

print("Happy Birthday to you!")

for i in range(age):
    print(f"Are you {i+1}")
"""

# get age input from user
age = input("How old are you?")
# convert age from a string to an int
age = int(age)

# print happy birthday
print("Happy Birthday to you!")

# using x as a counter variable to compare against user input age variable
x = 0
# while loop to print a statement based on the age input
while (x < age):
    # prints x + 1 to loop through the ages until you get to the user input age
    print(f"Are you {x+1}?")
    # iterating the counter variable, eventually reaches the user input age and ends the loop
    x += 1

