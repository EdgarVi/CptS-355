# Programmer: Edgar Villasenor
# WSU ID: 11536698
# CptS 355 HW 3
# 17 October 2019

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

# 1c. addNLogs()
if __name__ == '__main__':
    log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
    sprintLog(log1)
    print("hello HW 3")