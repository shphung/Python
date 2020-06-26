#!/usr/bin/python


#gets the larger one of two integers

def larger (x, y) :
	if x > y :
		return x
	else :
		return y

def main():
    num1 = int(input("Please enter the first integer: "))
    num2 = int(input("Please enter the second integer: "))
    print("The larger one is: ", larger(num1, num2))

if __name__ == "__main__":
	main()#

