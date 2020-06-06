'''
    File: Assignment2_Problem1.py
    Author: Steven Phung
    Class: CS 2520.01 - Python for Programmers

    Assignment: Assignment 2
    Completed (or Last Revision): 2/16/20

    Purpose: Practicing functions
    Text analyzer & modifier
    Implement:
    get_num_of_characters(): which takes a string as a parameter and returns
    the number of characters in the user's string.
    
    output_without_whitespace(): which takes a string as a parameter and outputs
    the string's characters except for whitespaces (spaces and tabs)
    
    get_acronym(): which returns the acronym for a phrase. e.g. acronym
    for "random access memory" is RAM, acronym for "central processing unit" is
    CPU.
    
    main() function that first prompts the user to enter a sentence of their
    choice, output the string, and calls the functions get_num_of_characters()
    and output_without_whitespace() to get character counts as well as output
    without whitespaces, then prompts the user again for a prhase and output
    the acronym
'''

#Function: get_num_of_characters(string)
#Purpose: return int number of characters in a string
def get_num_of_characters(inputString) :
    totalChars = 0
    for char in inputString :
        totalChars += 1
    return totalChars

#Function: output_without_whitespace(string)
#Purpose: return input string excluding tab / spaces
def output_without_whitespace(inputString) :
    newString = ""
    for char in inputString :
        if char == ' ' or char == '\t' :
            pass
        else:
            newString = newString + char
    return newString

#Function: get_acronym(string)
#Purpose: return new string as amalgamation of the first letter of all words in input string
def get_acronym(inputString) :
    acronym = ""
    wordList = inputString.split()
    for words in wordList :
        acronym = acronym + words[0].upper()
    return acronym

#Function: main()
#Purpose: test all functions
def main() :
    userInput = input("Enter a sentence or a phrase: ")
    print("You entered:", userInput)
    print("Character count: ", get_num_of_characters(userInput))
    print("No whitespace: ", output_without_whitespace(userInput))
    userInput = input("Enter a sentence or a phrase: ")
    print("Acronym: ", get_acronym(userInput))
    
main()

'''
Test cases: 

Enter a sentence or a phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.
Character count:  46
No whitespace:  Theonlythingwehavetofearisfearitself.
Enter a sentence or a phrase: random access memory
Acronym:  RAM

Enter a sentence or a phrase: This is a tab		to test tabs. As well as 123s and !@#s.
You entered: This is a tab              to test tabs. As well as 123s and !@#s.
Character count:  54
No whitespace:  Thisisatabtotesttabs.Aswellas123sand!@#s.
Enter a sentence or a phrase: Real time strategy
Acronym:  RTS

Enter a sentence or a phrase: 
You entered: 
Character count:  0
No whitespace:  
Enter a sentence or a phrase: 
Acronym:  
'''