# Programmer: Edgar Villasenor
# WSU ID: 11536698
# CptS 355 Programming Language Design
# 8 November 2019

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  # define the top of stack as the end of the list

# returns the popped value
def opPop():
    return opstack.pop()

# pushes value to opstack
def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# definition of dictstack and associated operations
dictstack = []   # define the top of stack as the end of the list

# dictPop pops the top dictionary from the dictionary stack.
def dictPop():
    return dictstack.pop()

# dictPush pushes the dictionary ‘d’ to the dictstack. 
def dictPush(d):
    dictstack.append(d)
    
# add "name:value" pair to the top dictionary in the dictionary stack. 
def define(name, value):
    i = len(dictstack)
    if(i != 0):
        i -= 1
        dictstack[i][name] = value # add the pair to top dictionary in dictstack
    else:
        d = {name:value}
        dictPush(d)

# returns the value associated with name
def lookup(name):
    if(name[0] != '/'):
        name = '/' + name
    for d in reversed(dictstack):
        if d.get(name) != None:
            return d[name]
    
    # if the value is not found in the dictstack, raise an exception so the program doesn't crash
    raise Exception('key ' + '\'' + name + '\'' + ' was not found in dictstack') 
    


#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt

def add():
    op1 = opPop()
    op2 = opPop()
    res = op1 + op2
    opPush(res)

def sub():
    op1 = opPop()
    op2 = opPop()
    res = op2 - op1
    opPush(res)

def mul():
    op1 = opPop()
    op2 = opPop()
    res = op1 * op2
    opPush(res)

def div():
    op1 = opPop()
    op2 = opPop()
    if(type(op1) != int or type(op2) != int):
        raise Exception("Both values must be integers")
    res = op2 / op1
    opPush(res)

def eq():
    op1 = opPop()
    op2 = opPop()
    res = False
    if op1 == op2:
        res = True
    opPush(res)

def lt():
    op1 = opPop()
    op2 = opPop()
    res = False
    if op1 >= op2:
        res = True
    opPush(res)

def gt():
    op1 = opPop()
    op2 = opPop()
    res = False
    if op1 <= op2:
        res = True
    opPush(res)

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, put, aload, astore

# returns the list of the SPS array in the opstack
def length():
    tup = opPop() # for now assume array is always top element, fine for current test casess
    l = tup[0]
    opPush(l)


# returns the indexed element on the top of the stack
def get(): 
    i = opPop() # grab index from top of stack
    tup = opPop() # grab array tuple from top of stack
    res = tup[1][i] # extract value at index i
    opPush(res)
    return res

# removes the two values and the array object from stack
# puts value at index of array
def put():
    val = opPop() # value to replace with
    i = opPop() # index
    tup = opPop() # array tuple

    tup[1][i] = val

    opPush(tup)
    
# removes the array from stack, pushes every value onto the 
# stack then pushes the array back onto the stack
def aload():
    tup = opPop()
    ar = tup[1]

    sz = len(ar)
    i = 0
    while(i < sz):
        opPush(ar[i])
        i += 1
    opPush(tup)

# removes the array from the stack
# pops as many values from the stack as the length
# of the array, stores those values in the array 
# pushes array back to stack
def astore():
    tup = opPop()
    alength = tup[0]
    i = 0
    ar = []
    while i < alength:
        ar.append(opPop())
        i += 1
    ar.reverse()
    t = (tup[0], ar)
    
    opPush(t)
#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack

# duplicate the top value of the stack and push it on to the top of the stack
def dup():
    if len(opstack) == 0:
        return None
    res = opPop()
    opPush(res)
    opPush(res)
    return res

def copy():
    i = opPop() # number of values to copy
    j = len(opstack) - 1 # list index
    q = []
    while i > 0:
        q.append(opstack[j])
        i -= 1
        j -= 1
    
    j = len(q) - 1
    while j >= 0:
        opPush(q[j])
        j -= 1
    

def count():
    sz = len(opstack)
    opPush(sz)

def pop():
    return opPop()

# clear the stack
def clear():
    sz = len(opstack) - 1
    while(sz >= 0):
        opPop()    
        sz -= 1

# swaps the top two stack values
def exch():
    v1 = opPop()
    v2 = opPop()
    opPush(v1)
    opPush(v2)

# display contents of the stack starting from the top
def stack():
    i = len(opstack)
    while i >= 0:
        print(opstack[i])
        i -= 0

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

# takes one operand from the operand stack, ignores it, and creates a new empty dictionary
# on the operand stack
def psDict():
    opPop()
    d = {}
    opPush(d)

def begin():
    d = opPop()
    dictPush(d)

def end():
    dictPop()

# pop name and value from opstack and call define()
def psDef():
    vl = opPop()
    nm = opPop()
    if(type(nm) != str):
        raise Exception("Name must be a string")

    define(nm, vl) # push to dictstack