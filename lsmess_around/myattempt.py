from sys import argv
import re

def read_code():
    filename = argv[1]
    with open(filename,"r") as f: return f.read().split("\n")

def run():
	code = read_code() #each line of code as string array element
	if check_if_linear(code):
		print 'Linear' 
	elif check_if_constant(code):
		print 'Constant'

def check_if_linear(c):
	linear_hints = ["for","while", "in", "xrange", "range"]
	for line in c:
		words = line.split()
		print words
		for hint in linear_hints:
			if hint in line:
				return True
			continue
	return False

def check_if_constant(c):
	const_hints = ["[","]", "append", "pop" , "="]
	for line in c:
		words = line.split()
		for hint in const_hints:
			if hint in line:
				return True
			continue
	return False

if __name__ == '__main__':
    run()