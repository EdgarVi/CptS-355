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


"""
So you're given a list of dev sprintLogs
First need to run sprintLog on each list element (a dict)
"""
# 1c. addNLogs(logList)
def addNLogs(logList):
    
    sprintList = map (sprintLog, logList) # convert logList to desired format
    d = functools.reduce(addSprints, sprintList)
    return d
if __name__ == '__main__':
    log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
    sprintLog(log1)
    print("hello HW 3")