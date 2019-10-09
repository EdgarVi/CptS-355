#Strings
s1 = "This is a long string"
s2 = "!"
len(s1)
s1[-1]
s1[0:4]
s1[-1:]
s = s1 + s2
s.split( ' ' , 1)
s.split( ',' , 1)

#strings are immutable
s1[0] = 't'    #wont work

##############################################################
#Lists:
numbers = [1,2,3,4,5,6]
stuff = ["a", 1 , "355", [1,2,3], ["A",10]]
stuff[4]
stuff[-1]
[1,2,3,4,5,6][2:-2]

[1,2,3,4,5,6][2]      # returns 3
[1,2,3,4,5,6][2:3]    # returns [3]

# Nested lists:
LL = [[1,2,3],[4,5,6],['a','b','c']]
LL[1]
LL[1][:-1]

# Unlike strings, lists are mutable type, i.e. it is possible to change their content:
numbers = [0,1,2,0,0,5,6,0]
numbers[-1] = 7
numbers[3:5] = [3,4]
numbers[3:5] = []
numbers[ len (numbers)] = 10
numbers = numbers + [10,11]
numbers.append(10)

##############################################################
#Tuples:
(3,4)
(3,)  # tuple with a single value  
(3)   # not a tuple
(2,'A',3,4)[1:3]  #we can do slicing with tuples

# Python tuples are immutable
t = (1,2,3,4,5)
t[2] = 6    # will give an error

##############################################################
# Sorting lists

# Sorted is a builtin function that you can sort lists. It returns a new list(this is important) where the items in the list are sorted.
# Sorted doesn't change the original list.
L = [3,7,6,2,1]
sorted (L)
T = (3,7,6,2,1)
sorted (T3)

# You can sort it backwards.
sorted (L,reverse = True )

#we can also sort a lits using its sort method; sort will change the original list. 
L = [3,7,6,2,1]
L.sort()

##############################################################
#Functions
#You can create functions with the def keyword.
def nothing (n):
    pass

def sum (x,y):
    return x + y
sum ( 3 , 4 )

def getItem (t):
    return t[1]

getItem ( (1,'a') )

# In Python, types are checked at run-time
# the below will work
getItem ( (1,'a') )
getItem ( [2,'b'] )
getItem ( "3c" )

##############################################################
# Anonymous functions:
(lambda x : x+1)
(lambda x : x+1) (2)
(lambda item: item[1])

# sorting list of tuples
myL = [('a',3), ('b',2), ('f',1),('d',1), ('e',1), ('c',1)]
sorted(myL)
sorted(myL, key = lambda item: item[1])

# sort first on the second value then the first
sorted(sorted(myL), key = lambda item: item[1])