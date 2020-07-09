#   File: Lab4.py
#   Author: Steven Phung
#   Class: CS 2520.01 - Python for Programmers

#   Assignment: Lab 4
#   Completed (or Last Revision): 3/5/20

#   Purpose: Practicing list and tuple structures
import statistics

#Function: minimum(dataList)
#Purpose: Reads in list and returns lowest value from list
def minimum(dataList) :
    minValue = dataList[0]
    for x in dataList :
        if minValue > x :
            minValue = x
    return minValue

#Function: maximum(dataList)
#Purpose: Reads in list and returns highest value from list
def maximum(dataList) :
    maxValue = dataList[0]
    for x in dataList :
        if maxValue < x :
            maxValue = x
    return maxValue

#Function: getRange(dataList)
#Purpose: Returns range from values in a list using max-min formula
def getRange(dataList) :
    return maximum(dataList) - minimum(dataList)
    
#Function: mean(dataList)
#Purpose: Returns average of list, find sum then divide by n-# of values
def mean(dataList) :
    total = 0
    length = 0
    for x in dataList :
        total += x
        length += 1
    return total / length
    
#Function: median(dataList)
#Purpose: Returns median of list, first sort list
#If list contains even amount, there is no exact middle value
#so add two most-middle values and divide by 2 for median
#If list contains odd amount, return middle value
def median(dataList) :
    dataList.sort()
    length = 0
    for x in dataList :
        length += 1
    if length % 2 == 0 :
        return ((dataList[(length//2)-1] + dataList[(length//2)])/2)
    else :
        return dataList[length//2]

#Function: test1(dataList)
#Purpose: Tests all self-defined functions
#Also checks if given dataList is a list and non-empty before running tests
def test1(dataList) :
    reset()
    print("Test 1 for", dataList)
    if type(dataList) is list :
        if not dataList :
            print("List is empty.")
            print("")
        else :
            print("Min value: ", minimum(dataList))
            print("Max value: ", maximum(dataList))
            print("Range: ", getRange(dataList))
            print("Mean: ", mean(dataList))
            print("Median: ", median(dataList))
            print("")
    else :
        print("You did not pass a list. Cannot compute.")
        print("")
        
#Function: test1(dataList)
#Purpose: Tests statistics' module defined functions
#Also checks if given dataList is a list and non-empty before running tests
def test2(dataList) :
    reset()
    print("Test 2 for", dataList)
    if type(dataList) is list :
        if not dataList :
            print("List is empty.")
            print("")
        else :
            print("Min value: ", min(dataList))
            print("Max value: ", max(dataList))
            print("Range: ", getRange(dataList))
            print("Mean: ", statistics.mean(dataList))
            print("Median: ", statistics.median(dataList))
            print("")
    else :
        print("You did not pass a list. Cannot compute.")
        print("")

#Function: reset()
#Purpose: median function sorts given lists
#This is to reset each list to their inital state to ensure correct testing
def reset() :
    global d1, d2, d3, d4, d5
    d1 = [37, 32, 46, 28, 37, 41, 31]
    d2 = [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
    d3 = []
    d4 = "abc"
    d5 = [2.5, "abc", 4]

#Main
if __name__ == "__main__" :
    reset()
    test1(d1)
    test2(d1)
    
    test1(d2)
    test2(d2)
    
    test1(d3)
    test2(d3)
    
    test1(d4)
    test2(d4)
    
    #test1(d5)     #Type error
    #test2(d5)     #Type error

'''
Test1 and Test2 for d5 commented out

Test 1 for: [37, 32, 46, 28, 37, 41, 31]
Min value:  28
Max value:  46
Range:  18
Mean:  36.0
Median:  37

Test 2 for: [37, 32, 46, 28, 37, 41, 31]
Min value:  28
Max value:  46
Range:  18
Mean:  36
Median:  37

Test 1 for: [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
Min value:  0.5
Max value:  25
Range:  24.5
Mean:  5.933999999999999
Median:  4.65

Test 2 for: [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
Min value:  0.5
Max value:  25
Range:  24.5
Mean:  5.934
Median:  4.65

List is empty.

List is empty.

You did not pass a list. Cannot compute.

You did not pass a list. Cannot compute.
'''

'''
Test1 and Test2 with d5 results in type error

runfile('E:/Steven/CSU Pomona Files/Year 6/17 Spring 2020/CS2520 [Python]/Lab 4/Lab4.py', wdir='E:/Steven/CSU Pomona Files/Year 6/17 Spring 2020/CS2520 [Python]/Lab 4')
Test 1 for: [37, 32, 46, 28, 37, 41, 31]
Min value:  28
Max value:  46
Range:  18
Mean:  36.0
Median:  37

Test 2 for: [37, 32, 46, 28, 37, 41, 31]
Min value:  28
Max value:  46
Range:  18
Mean:  36
Median:  37

Test 1 for: [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
Min value:  0.5
Max value:  25
Range:  24.5
Mean:  5.933999999999999
Median:  4.65

Test 2 for: [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
Min value:  0.5
Max value:  25
Range:  24.5
Mean:  5.934
Median:  4.65

List is empty.

List is empty.

You did not pass a list. Cannot compute.

You did not pass a list. Cannot compute.

Test 2 for: [2.5, 'abc', 4]

TypeError: > not supported between instances of float and str
'''