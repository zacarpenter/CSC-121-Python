"""
Author:  Zac Carpenter
Course:  CSC 121
Assignment:  Lesson 08: Lab - Part 1
Purpose:  carpenterz08_part1.py
    This program asks the user for a
    file name. Then loops through the
    file and prints each line of the file.
Example file: CharNames.txt
"""


# try/except block to valiadate the file name input by the user
try:
    userInput = input("What file do you want to open? ")
    # open the file in 'read' mode
    fhandle = open(userInput, 'r')

    # loop through each line and print the formatted line
    for line in fhandle:
        cleanLine = line.rstrip()
        print(cleanLine)
    # close the file
    fhandle.close()
except:
    print("The file name entered does not exist.")
