from sys import argv
import re
def read_code():
    filename = argv[1]
    with open(filename,"r") as f: return f.read().split("\n")

def test_runtime():
    for ind,line in enumerate(code):
        #conditions that would imply O(n)
        conditions = [
            ["for","xrange"],
            ["for","range"],
            ["for","in","[","]"]
        ]
        #conditions that might violate O(n)
        anti_conditions = ["(\d,\d,\d)"]
        big_o_squared = False
        for condition in conditions:
            if all([elem in line for elem in condition]):
                if all([elem in code[ind+1] for elem in condition]): big_o_squared = True

        if any([re.search(elem,line) for elem in anti_conditions]):
            continue
        print "O(n^2) complexity found on line:",ind
        break
        if big_o_squared or any([re.search(elem,line) for elem in anti_conditions]):
            continue
        print "O(n) complexity found on line:",ind
        break
    
def poly_runtime(code,ind,conditions,counter=0):
    for condition in conditions:
        if not all([elem in code[ind] for elem in condition]):
            return "O(n^"+str(counter)+") complexity found on line:",ind
        else:
            return poly_runtime(code,ind+1,conditions,counter+1)

#To Do:
#1)
 # Run the source code you are analyzing through python dissembler module and look for break ops with the block of code under inspection
#2)
 # Add looking through while loops.  check the boolean while loop condition for variable names and look for how this is incremented in the remainder of the block.  Also look for break statements.

#3)
 # add something that looks for the source for a given function and then expands the current code to include the function's definition in the current function
        
def run():
    code = read_code()
    conditions = [
        ["for","xrange"],
        ["for","range"],
        ["for","in","[","]"]
    ]

    ind = 0 
    while ind < len(code)-1:
        result,ind = poly_runtime(code,ind,conditions)
        print result, ind
        ind += 1

if __name__ == '__main__':
    run()
