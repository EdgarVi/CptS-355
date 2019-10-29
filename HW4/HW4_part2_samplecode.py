import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(c)
    return False



# COMPLETE THIS FUNCTION
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
        else:
            res.append(c)
    return res

# COMPLETE THIS FUNCTION 
# Write auxiliary functions if you need them. This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
def interpretSPS(code): # code is a code array
    pass


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


#testing

input1 = """
        /square {dup mul} def 
        [-5 -4 3 -2 1] dup aload length 0 exch -1 1 
        {pop exch square add} for 
        55 eq stack
        """

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

input4 = """
            /sumArray { 0 exch aload length -1 1 {pop add} for } def
            /x 5 def
            /y 10 def 
            [1 2 3 4 x] sumArray
            [x 7 8 9 y] sumArray
            [y 11 12] sumArray
            [0 0 0] astore
            stack 
        """

input5 = """
            1 2 3 4 5 count copy 15 1 1 5 {pop exch sub} for 0 eq  
            stack 
            """

input6 = """
            /pow2 {1 dict begin 
                     /x exch def 
                     1 x -1 1 {pop 2 mul} for  
                   end } def
            [1 2 3 4 5 6 7] dup /A exch def
            0 1 A length 1 sub { /n exch def A n get pow2 /x exch def A n x put } for 
            A
            stack
            """

print(tokenize(input1))
print(parse(tokenize(input1)))

