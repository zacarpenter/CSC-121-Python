"""
Author:  Zac Carpenter
Course:  CSC 121
Assignment:  Lesson 08: Lab - Part 2
Purpose:  carpenterz08_part2.py
    This program takes a user file name as input
    to read the file. The program ask the user to input a
    'Title' of the character names in the file. Then loops
    through the file to find instances of that title.
    Displays the character names with that title and a
    final count.
Example file: CharNames.txt
"""


# try/except block to valiadate the file name input by the user
try:
    fileNameInput = input("What file do you want to open? ")
    # open the file in 'read' mode
    fhandle = open(fileNameInput, 'r')

    # get the title to display from user and initialize the counter
    charTitleInput = input("Enter the name of a title (i.e. Count, Duke, Chancellor, etc.): ")
    count = 0

    # loop through each line and count the number of characters with that title
    for line in fhandle:
        cleanLine = line.rstrip()
        # conditional to determine if the line contains the user input title
        if cleanLine.startswith(charTitleInput):
            count = count + 1
            print(cleanLine)

    # close the file
    fhandle.close()
    print(str(count) + ' characters had the title ' + charTitleInput)
except:
    print("The file name entered does not exist.")

