"""
Author:  Zac Carpenter
Course:  CSC 121
Assignment:  Lesson 04: Lab - Part 2 Counting Correct Guesses
Purpose:  carpenterz04-guess.py
	This program stores eye color, hair color,
    and number of pets you have. Then asks
    the user to guess them one by one. Finally,
    it displays the number of correct guesses the
    user input.
"""
# creating variables for the correct answers
eyeColor = "green"
hairColor = "brown"
numberOfPets = 2

# creating variables to store the inputs to the questions
answer1 = input("What is my eye color? ")
answer2 = input("What color is my hair? ")
answer3 = input("How many pets do I have? ")
# converting answer3 to type int so it matches the type of my variable for comparison
answer3 = int(answer3)

# create a variable to store the number of correct answers
correctAnswers = 0

# created separate if statements to check that each variable was correct and iterate the correctAnswers variable
# also used .lower() to ensure the variable's case matched for comparison
if answer1.lower() == eyeColor:
    correctAnswers += 1
if answer2.lower() == hairColor:
    correctAnswers += 1
# didn't need .lower() because I already changed answer3 to a type int()
if answer3 == numberOfPets:
    correctAnswers += 1

# just for testing I'm printing correctAnswers to see the value is iterating properly
#print(correctAnswers)

# created another if/elif/else block to determine final output
if correctAnswers >= 3:
    print("You guessed them all")
elif correctAnswers >= 1:
    print("You got some, but not all correct")
else:
    print("You didn't get any right")

