# Programmer: Edgar Villasenor
# WSU ID: 11536698
# CptS 355 HW 3
# 17 October 2019
import functools 
debugging = False
def debug(*s):
    if debugging:
        print(*s)


# 1) Dictionaries
# 1a. sprintLog(sprnt)
def sprintLog(sprnt):
    d = {}
    # use iterator for each dev in sprnt
    for dev in sprnt.keys():
        for task in sprnt[dev].keys():
            if(d.get(task) == None):
                d[task] = {}
                d[task][dev] = sprnt[dev][task] # sprnt[dev][task] is the hour value
            else:
                d[task][dev] = sprnt[dev][task]
    return d

# 1b. addSprints(sprint1, sprint2)
def addSprints(sprint1, sprint2):
    d = sprint1
    for task in sprint2.keys():
        if(d.get(task) == None): # task is not in sprintLog
            d[task] = sprint2[task] # add task to sprintLog
        else:
            # task is in d, merge tasks
            for dev in sprint2[task].keys():
                if(d[task].get(dev) == None):
                    d[task][dev] = sprint2[task][dev]
                else:
                    taskTime = d[task][dev] + sprint2[task][dev]
                    d[task][dev] = taskTime
    return d

# 1c. addNLogs(logList)
def addNLogs(logList):
    
    sprintList = map (sprintLog, logList) # convert logList to desired format
    d = functools.reduce(addSprints, sprintList)
    return d

# 2a. lookupVal(L, k)
def lookupVal(L, k):
    
    # not sure why the prompt asks for
    # the value closer to the end
    for x in reversed(L):
        if(x.get(k) != None):
            return x.get(k)
    return None

# 2b. lookupVal2(tL, k)
def lookupVal2(tL, k):
    i = len(tL)
    i -= 1

    while(i != -1):
        tup = tL[i]
        if(tup[1].get(k) != None):
            return tup[1].get(k)
        else:
            if(i == 0):
                i = -1 # stop the loop
            else:
                i = tup[0]
    return None

# 3. unzip(L)
def unzip(L):

    l1 = map((lambda tup: tup[0]), L )
    l2 = map((lambda tup: tup[1]), L )
    l3 = map((lambda tup: tup[2]), L )
    tup = (list(l1), list(l2), list(l3))
    return tup

# 4. numPaths(m, n, blocks)
def numPathsHelper(m, n, verticalIndex, horizontalIndex, blocks):
    if(verticalIndex == m and horizontalIndex == n): # terminate
        return 1
    
    down = 0
    right = 0
    
    # move down
    # check if location valid, if so, recurse down
    if((verticalIndex) <= m):
        verticalIndex += 1
        # search for tuple 
        if((verticalIndex, horizontalIndex) in blocks):
            pass
        else:            
            down = numPathsHelper(m, n, verticalIndex, horizontalIndex, blocks) 
            verticalIndex -= 1 # toggle index

    # move down
    # check if location valid, if so, recurse right
    if((horizontalIndex) <= n):
        horizontalIndex += 1
        if((verticalIndex, horizontalIndex) in blocks):
            pass
        else:
            right = numPathsHelper(m, n, verticalIndex, horizontalIndex, blocks)
            horizontalIndex -= 1 
    # return the result of recursion
    return down + right 

def numPaths(m, n, blocks):

    return numPathsHelper(m, n, 1, 1, blocks)
    
# 5a. iterFile()
class iterFile():
    def __init__(self, filename):
        self.fileobject = open(filename, "r")
        pass

    def __next__(self):
        buf = self.fileobject.read(1)
        s = ""
        if buf in ['\n', '\r\n', ' ', '']:
            print("empty line")

        while(buf != " "):
            s += buf
            buf = self.fileobject.read(1)

        return s

    def __iter__(self):
        return self

# 5b. wordHistorgram(words)
def wordHistorgram(words):
    pass

if __name__ == '__main__':
    #print("Run HW3SampleTests.py to unit test this code!")
    it = iterFile("testfile.txt")
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()
    wrd = it.__next__()


