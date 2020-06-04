'''
    File: Assignment1_Task1.py
    Author: Steven Phung
    Class: CS 2520.01 - Python for Programmers

    Assignment: Assignment #1_Task #1

    Purpose: Practicing if statements.
        BMI can be calculated using Imperial (American) or Metric (English)
    system. Note that we'd like the user to choose whether to use Imperial or
    Metric system.
    
        A BMI scale can be used to determine an individual's fitness status.
    Normally the scale is related to age, sex, etc. For simplicity, we will use
    18-25 as normal range, higher than that will be considered as overweight
    and lower than that will be considered as underweight. Please provide the
    user some feedback based on the calculated BMI.
    
    BMI Formula
    Imperial:       BMI = 703 * (weight (lb) / height^2 (in^2))
    Metric:         BMI = (weight (kg) / height^2 (m^2))
'''

imperialOrMetricSystem = int(input("1. Imperial (lb)\n2. Metric (kg)\nChoose Option: "))
#Ask again until valid option is provided
while not imperialOrMetricSystem == 1 and not imperialOrMetricSystem == 2 :
    print("Not a valid choice, please try again.")
    imperialOrMetricSystem = int(input("1. Imperial (lb)\n2. Metric (kg)\nChoose Option: "))

#Imperial formula
if imperialOrMetricSystem == 1 :
    weight = float(input("Please enter your weight (lb): "))
    
    #Weight must be between a small baby's weight (5lbs)
    #and the heaviest person ever recorded (1,400lbs)
    while not 5 <= weight <= 1400 :
        weight = float(input("Please enter a reasonable weight (lb): "))
        
    height = float(input("Please enter your height (in): "))
    
    #Height must be between a small baby's height (18in)
    #and tallest person ever recorded (107in)
    while not 18 <= height <= 108 :
        height = float(input("Please enter a reasonable height (in): "))
        
    #BMI formula
    bmi = 703 * (weight / height**2)
    
#Metric formula
elif imperialOrMetricSystem == 2 :
    weight = float(input("Please enter your weight (kg): "))
    
    #Weight must be between a small baby's weight (2.2kg)
    #and the heaviest person ever recorded (635kg)
    while not  2.2 <= weight <= 635 :
        weight = float(input("Please enter a reasonable weight (kg): "))
        
    height = float(input("Please enter your height (m): "))
    
    #Height must be between a small baby's height (0.457m)
    #and tallest person ever recorded (2.73m)
    while not 0.457 <= height <= 2.73 :
        height = float(input("Please enter a reasonable height (m): "))
        
    #BMI formula
    bmi = (weight / height**2)

#Print BMI result and range
print("Your BMI is: " + str(round(bmi, 2)))
if bmi >= 18 and bmi <= 25 :
    print("This is considered normal.")
elif bmi < 18 :
    print("This is considered underweight.")
elif bmi > 25 :
    print("This is considered overweight.")

'''
Tests

Underweight test
1. Imperial (lb)
2. Metric (kg)
Choose Option: 1
Please enter your weight (lb): 82
Please enter your height (in): 60
Your BMI is: 16.01
This is considered underweight.

Normal weight test
Choose Option:
1. Imperial (lb)
2. Metric (kg)
Choose Option: 2
Please enter your weight (kg): 69
Please enter your height (m): 1.76
Your BMI is: 22.28
This is considered normal.

Overweight test
Choose Option:
1. Imperial (lb)
2. Metric (kg)
Choose Option: 1
Please enter your weight (lb): 236
Please enter your height (in): 67
Your BMI is: 36.96
This is considered overweight.

Abnormal input #1
1. Imperial (lb)
2. Metric (kg)
Choose Option: 1
Please enter your weight (lb): 0
Please enter a reasonable weight (lb): -1
Please enter a reasonable weight (lb): 100000000
Please enter a reasonable weight (lb): 99
Please enter your height (in): 0
Please enter a reasonable height (in): -1
Please enter a reasonable height (in): 222222222
Please enter a reasonable height (in): 60
Your BMI is: 19.33
This is considered normal.

Abnormal input #2
1. Imperial (lb)
2. Metric (kg)
Choose Option: 2
Please enter your weight (kg): 0
Please enter a reasonable weight (kg): -1
Please enter a reasonable weight (kg): 999999999
Please enter a reasonable weight (kg): 58
Please enter your height (m): 0
Please enter a reasonable height (m): -1
Please enter a reasonable height (m): 8888888888
Please enter a reasonable height (m): 1.645
Your BMI is: 21.43
This is considered normal.
'''