"""
Author:  Zac Carpenter
Course:  CSC 121
Assignment:  Lesson 06: Lab - Part 1 Sandwich Order with Validation Loop
Purpose:  carpenterz06_prog2.py
	This program creates a function that asks the user for a sandwich
    choice and then validates the input. The function returns the
    sandwich choice. A main function is created and displays our output.
"""
# create a function named choose_sandwich - takes no parameters
def choose_sandwich():
    # tell the user what type of sandwiches are available
    print("Your sandwich choices are: hamburger, cheeseburger, or chicken.")
    # get user input and store their answer in variable sandwich
    sandwich = input("What type of sandwich would you like? ")

    # input validation loop to determine the user input sandwich variable
    # is one of our sandwich options
    while (sandwich not in ['hamburger', 'cheeseburger', 'chicken']):
        # print a message letting the user know the input was invalid
        print("Sorry, but you must choose: hamburger, cheeseburger, or chicken.")
        # get user input again
        sandwich = input("What type of sandwich would you like? ")

    # returns the valid user input
    return(sandwich)

# create main function - takes no parameters
def main():
    # prints the welcome message
    print("Welcome to Elmo's Diner")
    # prints an f-string that displays the user choice by invoking choose_sandwich()
    print(f"Wonderful, for lunch today we will serve you: {choose_sandwich()}")
    # prints the thank you message
    print("Thank you for dining at Elmo's Diner")

# invoke main function
main()
