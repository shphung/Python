'''
    File: Assignment1_Task2.py
    Author: Steven Phung
    Class: CS 2520.01 - Python for Programmers

    Assignment: Assignment #1_Task #2

    Purpose: Practicing loops
        Use Monte-Carlo method (or other iterative method) to calculate Pi.
    The goal is to achieve a result (PI) as accurate as Math.pi to 0.000001
    (i.e. abs(your_pi – Math.pi) < 1.0e-6
    
        Reset random number seed at the beginning of your program. Do multiple
    iterations, for example, n = 1000, 10000, …. (choose your own n values) and
    show the intermediate results as well as the final result.

'''

from random import random
import math

#n values used for iterations
iterations = [5, 10, 100, 1000, 10000, 100000, 1000000]

#for each iteration value, use monte-carlo method to find pi estimate
for pointsInSquare in iterations :
    pointsInCircle = 0
    print("For n = " + str(pointsInSquare))
    #For 0 to n number of iterations
    for i in range(pointsInSquare) :
        #Generate random x and y
        x = random()
        y = random()
        diameter = x*x + y*y
        #if random point is inside circle, increment pointsInCircle
        if diameter <= 1 :
            pointsInCircle += 1
    #pi = 4 * (Points in circle / points in square)
    myPi = 4 * (pointsInCircle / pointsInSquare)
    #error
    error = abs(myPi - math.pi)
    print("Pi Estimate: " + str(myPi))
    print("Pi Estimate - Pi: " + str(round(error, 6)) + "\n")

'''
For n = 5
Pi Estimate: 3.2
Pi Estimate - Pi: 0.058407

For n = 10
Pi Estimate: 3.2
Pi Estimate - Pi: 0.058407

For n = 100
Pi Estimate: 2.88
Pi Estimate - Pi: 0.261593

For n = 1000
Pi Estimate: 3.148
Pi Estimate - Pi: 0.006407

For n = 10000
Pi Estimate: 3.16
Pi Estimate - Pi: 0.018407

For n = 100000
Pi Estimate: 3.14424
Pi Estimate - Pi: 0.002647

For n = 1000000
Pi Estimate: 3.142368
Pi Estimate - Pi: 0.000775
'''