from sys import argv
import re

def read_code():
    filename = argv[1]
    with open(filename,"r") as f: return f.read().split("\n")

def is_linear(c):
	linear_hints = ["for","while", "in", "xrange", "range"] ##common linear attributes
	for line in c:
		words = line.split()
		for word in words:
			for hint in linear_hints:
				if hint == word:
					return True
				continue
	return False

def is_constant(c):
	const_hints = ["[","]", "append", "pop" , "="]
	for line in c:
		words = line.split()
		for word in words:
			for hint in const_hints:
				if hint == word:
					return True
				continue
	return False

def is_logarithmic(c):
	##are we using a tree data structure?
	##are we binary searching?
	#is the loop-control-var being divided by 2 at each iteration?
	pass

def run():
	exp = ""
	code = read_code() #each line of code as string array element
	if is_linear(code):
		print 'O(n) complexity found' 
	elif is_constant(code):
		print 'O(1) complexity found'

if __name__ == '__main__':
    run()