""""
Program: word_count.py
Author: Tyrell Robbins
This program will take a txt file and count the total: lines, words, and characters with and without the whitespace

 """

# This line will ask the user to enter a filename to open
file_to_open = input("Please Enter the name of the file:")
# This line will open the requested file in read mode
#file = open(file_to_open, "r")


# Defining functions to count lines
def total_lines():
    file = open(file_to_open, "r")

    line_counter = 0 # variable to keep track of line count

    for line in file: # this for loop will count each line
        line_counter += 1
    print("Total number of lines:", line_counter)


# Defining function to count words
def total_words():
    file = open(file_to_open, "r")

    word_counter = 0 # variable to keep track of word count

    for line in file:
        words = line.split() # This will split the lines up into each word

        for word in words: # this will count the number of words

            word_counter += 1

    print("Total number of words:", word_counter)


# Defining function to count characters (White spaces not included)
def total_characters_with_white_space():
    file = open(file_to_open, "r")

    char_counter = 0 # variable to keep track of character count

    for line in file:
        words = line.split() # This will split the lines up into each word

        for word in words:

            char = word.strip()

            for char in word: # this for loop will count the number of characters

                char_counter += 1

    print("Total number of characters (excluding whitespace):", char_counter)


# Defining function to count characters (White spaces included)
def total_characters_without_white_space():
    file = open(file_to_open, "r")

    char_counter = 0 # variable to keep track of character count

    for line in file:
        words = line

        for word in words:

            for char in word: # this for loop will count the number of characters

                char_counter += 1

    print("Total number of characters (including whitespace):", char_counter)

# this section is where I will call the functions created.
#main


total_lines()
total_words()
total_characters_with_white_space()
total_characters_without_white_space()
