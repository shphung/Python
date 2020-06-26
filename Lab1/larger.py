#!/usr/bin/python

import sys

#gets the larger one of two integers

def larger (x, y) :
	if x > y :
		return x
	else :
		return y

def main():
	print( larger (int(sys.argv[1]), int(sys.argv[2])))

if __name__ == "__main__":
	main()#

