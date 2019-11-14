# Programmer: Edgar Villasenor
# WSU ID: 11536698
# CptS 355 Programming Language Design
# 8 November 2019

import re

# The operand stack: define the operand stack and its operations
opstack = []  # define the top of stack as the end of the list

# returns the popped value
def opPop():
    return opstack.pop()

# pushes value to opstack
def opPush(value):
    opstack.append(value)

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

# Array operators: define the string operators length, get, put, aload, astore

# remove array from stack and push it's length to stack
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

# Dictionary manipulation operators

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


# tokenize code array
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# The sequence of return characters is represented as list of properly nested
# tokens, where the tokens between '{' and '}' are included as a sublist. If the
# parentheses in the input iterator is not properly nested, return False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(c)
    return False

# if we encounter a '[' in the token, we have to create tuple of the elements
# note that it is a string in the form: '[5 4 3 -1 1]' so we need to tokenize it
def arrayMatching(it):
    arr = []
    it = it[:-1] # remove final ']' from string
    chars = it.split(' ') # chars is an array of tokens now

    for c in chars:
        arr.append(int(c))
    
    res = (len(arr), arr) # put into tuple
    return res



# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        elif c[0] == '[':
            arr = arrayMatching(c[1:]) # pass in rest of list
            res.append(arr)
        else:
            x = tryConvert(c) # try to convert from string to bool or int
            res.append(x)
    return res

# try to convert string to  corresponding value
def tryConvert(c):
    if c == 'false':
        return False
    elif c == 'true':
        return True
    try:
        v = int(c)
        return v
    except ValueError:
        pass
    return c


funDict = {
    "opPop": opPop,
    "dictPop": dictPop,
    "length": length,
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "eq": eq,
    "lt": lt,
    "gt": gt,
    "get": get,
    "dup": dup,
    "exch": exch,
    "pop": pop,
    "copy": copy,
    "clear": clear,
    "stack": stack,
    "dict": psDict,
    "begin": begin,
    "end": end,
    "def": psDef,
    "aload": aload
}

def psIf():
    codearray = opPop()
    boolVal = opPop()
    if isinstance(boolVal, bool) and boolVal == True:
        codearray = iter(codearray)
        interpretSPS(codearray)

def psIfelse(item):
    arr1 = opPop()
    arr2 = opPop()
    boolVal = opPop()
    if isinstance(boolVal, bool) and boolVal == True:
        arr2 = iter(arr2)
        interpretSPS(arr2)
    else:
        arr1 = iter(arr1)
        interpretSPS(arr1)

def psFor(item):
    arr = opPop()
    final = opPop()
    incr = opPop()
    init = opPop()

    i = init
    while i < final:
        opPush(i)
        i += incr
    opPush(i)
    interpretSPS(arr)

spsDict = {
    "if": psIf,
    "ifelse": psIfelse,
    "for": psFor,
}

# Heart of the interpreter, makes state changes to dictStack and opStack
def interpretSPS(codearray): # code is a code array
    try:
        item = next(codearray)
        if isinstance(item, str):
            if '/' in item:
                opPush(item)
            elif funDict.get(item, None) != None:
                funDict[item]()
            elif spsDict.get(item, None) != None:
                spsDict[item]()
            else:
                lookup(item)
        elif isinstance(item, list) or isinstance(item, (int, float, complex)) or isinstance(item, bool):
            opPush(item)
        return interpretSPS(codearray)
    except StopIteration:
        pass

def interpreter(s): # s is a string
    return interpretSPS(iter(parse(tokenize(s)))) # send code array to interpretSPS() as iterable
    

#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


def testInterpreter():
    clearStacks()
    input1 = """
        /square {dup mul} def 
        [-5 -4 3 -2 1] dup aload length 0 exch -1 1 
        {pop exch square add} for 
        55 eq stack
        """
    #print(parse(tokenize(input1)))
    #print(tokenize(input1)) 
    #print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))   
    print(interpreter(input1))
    clearStacks()


    input2 ="""
        /n 5 def
        /fact {
            0 dict begin
            /n exch def
            n 2 lt
            { 1}
            {n 1 sub fact n mul }
            ifelse
            end 
        } def
        n fact stack
        """

    print(interpreter(input2))
    clearStacks()


    input3 = """
            /fact{
                0 dict
                begin
                    /n exch def
                    1
                    n -1 1 {mul} for
                end
            } def
            6 fact stack
            """
    
    print(interpreter(input3))
    clearStacks()
    
    input4 = """
            /sumArray { 0 exch aload length -1 1 {pop add} for } 
            def/x 5 def
            /y 10 def 
            [1 2 3 4 x] sumArray
            [x 7 8 9 y] sumArray
            [y 11 12] sumArray
            [0 0 0] astore
            stack 
        """
    print(interpreter(input4))
    clearStacks()


    input5 = """
            1 2 3 4 5 count copy 15 1 1 5 {pop exch sub} for 0 eq  
            stack 
            """  
    print(interpreter(input5))
    clearStacks()

    input6 = """
            /pow2 {1 dict begin 
                    /x exch def 
                    1 x -1 1 {pop 2 mul} for  
                end } def
            [1 2 3 4 5 6 7] dup /A exch def
            0 1 A length 1 sub { /n exch def A n get pow2 /x exch def A n x put} for 
            A
            stack
            """  
    print(interpreter(input6))
    clearStacks()


def main():
    testInterpreter()
    
    
main()