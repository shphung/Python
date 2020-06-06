'''
    File: Assignment2_Problem2.py
    Author: Steven Phung
    Class: CS 2520.01 - Python for Programmers

    Assignment: Assignment 2

    Purpose: Practicing functions
    Write a program that asks the user to enter a zip code (in ZIP+4 format)
    then encode the zip code and print out the barcode (note: this is the old
    barcode format)
    
    Challenge (optional): Instead of ZIP+4, if a user enters just zip code say,
    55555, the program automatically will treat it as 55555-0000
'''
import digitprint

#Function: removeFromZip(String)
#Takes string as argument, removes '-' from the string, returns new string
#Return type: String
def removeFromZip(inputString) :
    newZip = ""
    for char in inputString :
        if char == '-' :
            pass
        else:
            newZip = newZip + char
    return newZip

#Function: generateCheckSum(String)
#generate check sum using given formula 10-sum mod 10, return check sum value
#Return type: int
def generateCheckSum(inputString) :
    sum = 0
    zip = int(inputString)
    while zip > 0 :
        remainder = zip % 10
        zip = zip // 10
        sum += remainder
    return 10 - (sum % 10)

#Function: printPostalBarCode(String)
#use digitprint module to print bar code based on zipcode string
def printPostalBarCode(zipcode) :
    digitprint.long()
    for digit in zipcode :
        if digit == '0' :
            digitprint.print_zero()
        elif digit == '1' :
            digitprint.print_one()
        elif digit == '2' :
            digitprint.print_two()
        elif digit == '3' :
            digitprint.print_three()
        elif digit == '4' :
            digitprint.print_four()
        elif digit == '5' :
            digitprint.print_five()
        elif digit == '6' :
            digitprint.print_six()
        elif digit == '7' :
            digitprint.print_seven()
        elif digit == '8' :
            digitprint.print_eight()
        elif digit == '9' :
            digitprint.print_nine()
    digitprint.long()

#Function: autoFillZip(String)
#Fill rest of zipcode / cut zipcode according to required format
def autoFillZip(zipcode) :
    
    #If entered zipcode value is empty, fill with zeroes
    if zipcode == "" :
        autoZip = ""
        for i in range(9) :
            autoZip = autoZip + '0'
    
    #If zipcode entered is not empty, assume it has a hyphen, so remove it
    zipWithoutHyphen = removeFromZip(zipcode)
    
    #If zipcode is less than 9 digits, add necessary 0's
    if 0 < len(zipWithoutHyphen) < 9 :
        autoZip = zipWithoutHyphen
        autoFillNeeded = 9 - len(zipWithoutHyphen)
        for i in range(len(zipWithoutHyphen), len(zipWithoutHyphen)+autoFillNeeded) :
            autoZip = autoZip + '0'
    #If zipcode is more than 9 digits, cut it down to 9
    elif len(zipWithoutHyphen) > 9 :
        autoZip = ""
        for i in range(9) :
            autoZip = autoZip + zipWithoutHyphen[i]
    #If zipcode is 9 digits exactly, keep as is
    else :
        autoZip = zipWithoutHyphen
        
    #Return correctly filled zipcode
    return autoZip

def main() :
    zipCode = input("Enter ZIP code: ")
    zipWithoutHyphen = removeFromZip(zipCode)
    
    #Zipcode has to only contain numerical values or user will be re-prompted
    while not zipWithoutHyphen.isnumeric() :
        zipCode = input("Enter numeric ZIP code: ")
        zipWithoutHyphen = removeFromZip(zipCode)
    else :
        formattedZipCode = autoFillZip(zipCode)

    #Generate check sum value
    checkDigit = generateCheckSum(formattedZipCode)
    
    #Append check sum value to zipcode
    zipWithCheckDigit = formattedZipCode + str(checkDigit)
    
    #Print out values and bar code
    print("Printing:", zipWithCheckDigit)
    printPostalBarCode(zipWithCheckDigit)
    digitprint.turtle.done()
    
main()