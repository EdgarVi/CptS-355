# Dictionaries:
d1 = { 1 :'a', 2 :'b', 3 :'c'}
d2 = {'a': 1 , 2 :'b', 3 :'c', 'c': 3 , 4 :'d'}

d2['a']
d2[2]
# d2[5]     # error, if you try to get the value of a key that doesnt exist in the dictionary, it generates an error.
d2.get(5)  # no error. It returns none.
d2.get(5,0)  # no error. It returns the provided default value : 0.

# Python dictionaries are mutable
# to add/update values to/in a dictionary 
d2[5] = 'f'  # add 5:'f' to dictionary
d2[2] = 'D'  # update the value for key 2 as 'D'

# values in a dictionary can be functions
def getFirst (t):
    return t[0]
def getSecond (t):
    return t[1]    

d3 = {1:getFirst, 2:getSecond}
d3[1]((1,"two"))
d3[2]((1,"two"))

# Can lists be dictionary keys?

# To get keys in dictionary:
d2.keys()
list (d2.keys())

# To get values in dictionary
d2.values()
list (d2.values())

# To get both:
d2.items()
list(d2.items())

#You can also sort dictionaries (Caution!):
d = {'c': 5 , 'a': 1 , 'b': 2 , 'd': 1 }
sorted (d)
di = list (d.items())
sorted (di)
sorted (di, key = lambda item: item[1])

# convert a list of tuples to a dictionary
d_sorted = dict(sorted(list (d.items())))


# range function 
rL = list (range(0,10))
rL = list (range(0,10,2))
rL = list (range(10,0,-1))

#for and while loop
myS = "CptS355"
myL = [1,2,"three",(4,5),[6,7,8],True]
numbers = [1,2,3,4,5,6,7,8]
myT = (1,2,"three",4,5,6,False)
myD = {"f":9,"d":3,"e":7,"a":1}
myClasses = {1:"355",2:"322",3:"451",4:"421"}

for i in range(0,len(myL)):
    print(myL[i])

for x in myS:
    print(x)

for k in myD.keys():
    print(k,myD[k])

for x in myD.items():
    print(x[0],x[1])

for k,v in myD.items():
    print(k,v)

cPairs = [('red',1), ('yellow',5),('blue',2)]
for (name,count) in cPairs:
   print('Color', name, 'appears', count, 'times')

cTriples = [('red',1,0xFF0000), ('yellow',5,0xFFFF00),('blue',2,0x0000FF)]
for (name,count,color) in cTriples:
   print('Color', name, 'appears', count, 'times', '-', color)


i = 0
x = myL[i]
while i < len(myL):
    print(x)
    x = myL[i]
    i +=1

i = 0
x = myL[i]
while i < len(myL):
    print(x)
    if x == "three":
        break
    x = myL[i]
    i +=1


# conditional statements
if "three" in myL:
    print("found")

c = "355"
if c == "355":
    print ("CptS",c)
elif c == "354":
    print ("EE",c)
else:
    print ("N/A")

list1 = [1,2,"three",(4,5),[6,7,8],True]
list2 = [1,2,"three",(4,5),[6,7,8],True]
list3 = list2
list4 = None

if list1 == list2:
    print("List values are equal!")

if list2 is list3:
    print("Lists are identical!")


# Class exercise

#def histo(s):
#    d = {}
#    for c in s:
#        d[c] = d.get(c,0) + 1
#    return sorted(list(d.items()),key=lambda item: -1*item[1])

# version 1
def histo(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1 # increment
        else:
            d[c] = 1 # initialize
    return sorted(sorted(list(d.items())), key = lambda item: item[1], reversed = True)


# List comprehension
numbers = [1,2,3,4,5,6]
letters = ['a','b','c','d','e','f']
squares = [x*x for x in numbers]
pairs = [(i,c) for i in numbers for c in letters]
intpairs = [(i1,i2) for i1 in numbers for i2 in numbers if i1<i2]

[x*x for x in numbers][2:5]

def histo2(s):
    return list(set([(c,s.count(c)) for c in s]))

# scope of local variables: global, and  nonlocal variables

# Is s a global or local variable? 
s = "CptS355"
def f(): 
    print(s)
    s = "CptS322"
    
#f()
print(s)

# Is s a global or local variable? 
# When f() is eecuted, will the value of the global s change?
s = "CptS355"
def f(): 
    global s
    print(s)
    s = "CptS322"
    
f()
print(s)


## global and local variables - example 1
z = 1
def f():
    z = 4
    def g(a):
        #print("z in g:",z)
        z =  10
        return z
    return z+g(19)

result1 = f()
print("example 1 - z in main:",z)

## global and local variables
z = 1
def f():
    z = 4
    def g(a):
        global z
        print("z in g:",z)
        z =  10
        return z
    return z + g(19)
result2 = f()
print("example 2 - z in main:",z)

## global, local, and nonlocal variables
z = 1
def f():
    z = 4
    def g(a):
        nonlocal z
        print("z in g:",z)
        z =  10
        return z
    return z + g(19)
result3 = f()
print("example 3 - z in main:",z)

#Additional examples

# dynamic typing
def demo (p):
	p[0] = 'c'
	return p

L = [1,2]
t = (1,2)
#result = demo(t)
#result = demo(L)
print("L:", L)
#print("result:",result)


# local vs global variables
def demo2(L):
	L=['a','b','c']
	return (L)

L = [1,2]
result = demo2(L)
print("L:", L)
print("result:",result)

# Patterns
p = ( 1 , 2 , 3 , 4 )
x,y,z,t = p

p = [ 1 , 2 , 3 , 4 ]
x,y,z,t = p

p = "1234"
x,y,z,t = p

x = 'a'
y = 'b'
z = 'c'
t = 'd'
p = (x,y,z,t)
p = [x,y,z,t]
p = x + y + z + t

# file operations

# To open a file use the open function:
f = open ("test.py", mode = 'r')  
lines = f . readlines()    # reads all the lines of a file into a list.

#An open file will also behave like a list in some contexts so you can write
for line in f:
    pass  # process one line
#or even

for line in open ("test.py"):
    pass # process one line

if __name__ == "__main__":
    h= histo("ABBCCCDDDDEEEEEFFFFFFGGGGGGG")
    print("histogram",h)