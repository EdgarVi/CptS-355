import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
    
        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.addedSprints = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}

        # addNLogs input/output
        self.logList = [self.log1,self.log2,self.log3,self.log4]
        self.sprintSummary = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20, 'Kelly': 20}, 'task6': {'Aaron': 8, 'Helen': 26, 'Alex': 15}}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # unzip input/output
        self.unzipInput = ([(1,"a",{1:"a" }),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d" ,{4:"d"})])
        self.unzipOutput = ([1, 2, 3, 4], ['a', 'b', 'c', 'd'], [{1 :'a' }, {2 :'b'}, {3 : 'c' }, {4 : 'd'}])
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
      
    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)
    
    
    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints)

    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList),self.sprintSummary)

    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)

    
    def test_lookupVal2(self):
        self.assertEqual(lookupVal2(self.lookup2List, "x"), 1)
        self.assertEqual(lookupVal2(self.lookup2List, "y"), False)
        self.assertEqual(lookupVal2(self.lookup2List, "z"), "zero")
        self.assertEqual(lookupVal2(self.lookup2List, "t"), None)
        
    

    def test_unzip(self):
        self.assertEqual(unzip(self.unzipInput), self.unzipOutput)

    
    def test_numPaths(self):
        self.assertEqual(numPaths(2,2,[(2,1)]), 1)
        self.assertEqual(numPaths(3,3,[(2,3)]), 3) 
        self.assertEqual(numPaths(4,3,[(2,2)]), 4) 
        self.assertEqual(numPaths(10,3,[(2,2),(7 ,1)]), 27)

    """
    def test_iterFile(self):
        mywords = iterFile("testfile.txt")
        self.assertEqual(mywords.__next__(),"CptS")  
        self.assertEqual(mywords.__next__(),"355")
        self.assertEqual(mywords.__next__(),"Assignment")
        restofFile = []
        for word in mywords:  
            restofFile.append(word)
        self.assertEqual(restofFile,self.filetokens[3:])

    def test_wordHistogram(self):
        pass
    """
if __name__ == '__main__':
    unittest.main()

