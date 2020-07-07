#   File: Lab3.py
#   Author: Steven Phung
#   Class: CS 2520.01 - Python for Programmers

#   Assignment: Lab 3
#   Completed (or Last Revision): 2/16/20

#   Purpose: Practicing functions

def posNegZero(n) :
    if n == 0 :
        return 0
    elif n > 0 :
        return 1
    else :
        return -1
    
def sqrCube(n=5, m=3) :
    return n**2, m**3
    
def main() :
    print(posNegZero(-5))
    print(posNegZero(0))
    print(posNegZero(6.5))
    print(posNegZero(+32))

    print(sqrCube())
    print(sqrCube(4))
    print(sqrCube(3,5))
    print(sqrCube(n=4,m=2))
    #print(sqrCube(n=4,2))

main()

'''
print(sqrCube(n=4,2))
                     ^
SyntaxError: positional argument follows keyword argument

-1
0
1
1
(25, 27)
(16, 27)
(9, 125)
(16, 8)
'''