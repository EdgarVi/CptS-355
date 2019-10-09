{-Haskell is available for Windows, Mac, and Linux. Here's the download page: http://www.haskell.org/platform/.
We will be using the HUnit unit testing package in CptS 355.  

Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "runTestTT tests" at the Haskell prompt.  -}

module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import HW2

{- Two useful functions in the HUnit package are assertEqual and assertBool.
The arguments to 'assertEqual' are:
      a descriptive string
      the expected value
      the value being tested
The arguments to 'assertBool' are:
      a descriptive string
      the boolean value being tested
-}

p1a_test1 = TestCase (assertEqual "merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]) ) 
p1a_test2 = TestCase (assertEqual "merge2 [1,2,3,4,5] [6,7,8,9,10]" [1,2,3,4,5,6,7,8,9,10] (merge2 [1,2,3,4,5] [6,7,8,9,10]))
p1a_test3 = TestCase (assertEqual "merge2 [1,2] [0,10,12]" [0,1,2,10,12] (merge2 [1,2] [0,10,12]))
p1a_test4 = TestCase (assertEqual "merge2 [1,2,3] []" [1,2,3] (merge2 [1,2,3] []))

p1b_test1 = TestCase (assertEqual "merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]) ) 
p1b_test2 = TestCase (assertEqual "merge2Tail [1,2,3,4,5] [6,7,8,9,10]" [1,2,3,4,5,6,7,8,9,10] (merge2Tail [1,2,3,4,5] [6,7,8,9,10]))
p1b_test3 = TestCase (assertEqual "merge2Tail [1,2] [0,10,12]" [0,1,2,10,12] (merge2Tail [1,2] [0,10,12]))
p1b_test4 = TestCase (assertEqual "merge2Tail [1,2,3] []" [1,2,3] (merge2Tail [1,2,3] []))

p1c_test1 = TestCase (assertEqual "mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]" [-3,-2,-1,1,2,3,4,5,8,9]  (mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]) )
p1c_test2 = TestCase (assertEqual "mergeN [[1,2], [10,12], [2,5,6,8,9]]" [1,2,2,5,6,8,9,10,12] (mergeN [[1,2], [10,12], [2,5,6,8,9]]))
p1c_test3 = TestCase (assertEqual "mergeN [[], [8,9], [6,7], [1,2,3,4,5]]" [1,2,3,4,5,6,7,8,9] (mergeN [[], [8,9], [6,7], [1,2,3,4,5]])) 

p2a_test1 = TestCase (assertEqual "getInRange (-5) 5 [10,5,0,1,2,-5,-10]" [0,1,2]  (getInRange (-5) 5 [10,5,0,1,2,-5,-10]) )
p2a_test2 = TestCase (assertEqual "getInRange (-1) 1 [-2,2,3,4,5]" [] (getInRange (-1) 1 [-2,2,3,4,5]) )
p2a_test3 = TestCase (assertEqual "getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11]" [4,5,6,7,8,9] (getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11]))
p2a_test4 = TestCase (assertEqual "getInRange (-5) 5 [-10,-5,0,5,10]" [0] (getInRange (-5) 5 [-10,-5,0,5,10]))

p2b_test1 = TestCase (assertEqual "countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]" 6 (countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]) )
p2b_test2 = TestCase (assertEqual "countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]" 3 (countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]) )
p2b_test3 = TestCase (assertEqual "countInRange 1 5 [[1,5],[1],[5],[]]" 0 (countInRange 1 5 [[1,5],[1],[5],[]]))

p3a_test1 = TestCase (assertEqual "addLengths (FOOT 2) (INCH 5)" (INCH 29) (addLengths (FOOT 2) (INCH 5)) ) 
p3a_test2 = TestCase (assertEqual "addLengths (YARD 3) (INCH (-3))"  (INCH 105) (addLengths (YARD 3) (INCH (-3))) ) 
p3a_test3 = TestCase (assertEqual "addLengths (YARD 3) (INCH 3)" (INCH 111) (addLengths (YARD 3) (INCH 3)))
p3a_test4 = TestCase (assertEqual "addLengths (FOOT 3) (FOOT 5)" (INCH 96) (addLengths (FOOT 3) (FOOT 5)))

p3b_test1 = TestCase (assertEqual "addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]" (INCH 262) (addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]) )
p3b_test2 = TestCase (assertEqual "addAllLengths [[FOOT 2], [FOOT 2, INCH 2], []]" (INCH 50) (addAllLengths [[FOOT 2], [FOOT 2, INCH 2], []]))
p3b_test3 = TestCase (assertEqual "addAllLengths []" (INCH 0) (addAllLengths []))

p4a_test1 = TestCase (assertEqual ("sumTree "++(show t1)) 32 (sumTree t1) ) 
t1_output = NODE 32 (NODE 15 (NODE 9 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 17 (LEAF 8) (LEAF 9))
p4a_test2 = TestCase (assertEqual ("sumTree"++(show myTree)) 6389 (sumTree myTree))
myTree_output = NODE 50 (NODE 25 (NODE 20 (NODE 40 (LEAF 1) (LEAF 8)) (NODE 21 (LEAF 21) (LEAF 33))) (NODE 4 (LEAF 11)(LEAF 99))) (NODE 75 (NODE 60 (NODE 1929 (LEAF 909)(LEAF 202))(NODE 333 (LEAF 98)(LEAF 1997))) (NODE 85 (LEAF 1001)(LEAF 2009)))


p4b_test1 = TestCase (assertEqual ("createSumTree "++ (show t1)) (t1_output) (createSumTree t1) ) 
p4b_test2 = TestCase (assertEqual ("createSumTree " ++ (show myTree)) (resultTree) (createSumTree myTree))

p5_test1 = TestCase (assertEqual ("foldListTree (+) 0 "++ (show t4)) 36 (foldListTree (+) 0 t4 ) ) 
p5_test2 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show t5)) "School-of-Electrical-Engineering-and-Computer-Science-WSU" (foldListTree (++) "" t5) ) 
p5_test3 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show lTree)) "The-quick-brown-fox-jumped-over-the-lazy-dog-edgar-is-thebee's-knees!" (foldListTree (++) "" lTree) ) 

{- 6- Create two tree values :  Tree Integer  and  listTree a ;  Both trees should have at least 3 levels. -}
-- Tree Integer
myTree = NODE 50
          (NODE 25 (NODE 20 (NODE 40 (LEAF 1) (LEAF 8)) (NODE 21 (LEAF 21) (LEAF 33))) (NODE 4 (LEAF 11)(LEAF 99)))
          (NODE 75 (NODE 60 (NODE 1929 (LEAF 909)(LEAF 202))(NODE 333 (LEAF 98)(LEAF 1997))) (NODE 85 (LEAF 1001)(LEAF 2009)))

-- calculated resultTree by hand, was a very tedious process
resultTree = NODE 6389
          (NODE 173 (NODE 63 (NODE 9 (LEAF 1) (LEAF 8)) (NODE 54 (LEAF 21) (LEAF 33))) (NODE 110 (LEAF 11)(LEAF 99)))
          (NODE 6216 (NODE 3206 (NODE 1111 (LEAF 909)(LEAF 202))(NODE 2095 (LEAF 98)(LEAF 1997))) (NODE 3010 (LEAF 1001)(LEAF 2009)))

-- List Tree
leaf1 = ListLEAF ["The","-","quick","-","brown"]
leaf2 = ListLEAF ["-","fox","-"]
leaf3 = ListLEAF ["jumped","-","over","-"]
leaf4 = ListLEAF ["the"]
leaf5 = ListLEAF ["-", "lazy", "-", "dog"]
leaf6 = ListLEAF ["-", "edgar", "-", "is", "-", "the", "bee's", "-knees!"]


node1 = ListNODE [leaf1,leaf2]
node2 = ListNODE [leaf3, leaf4]
node3 = ListNODE [leaf5,leaf6]
node4 = ListNODE []
node5 = ListNODE []
node6 = ListNODE []
node7 = ListNODE [node4, node5, node6]
node8 = ListNODE [node1, node2, node3]
node9 = ListNODE []
node10 = ListNODE [node7, node8]

lTree = ListNODE [node9, node10]


-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 3 levels. 
t1 = NODE 1
         (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) 
         (NODE 7 (LEAF 8) (LEAF 9))
t2 = NODE 0
          (NODE 0 (LEAF 4) (NODE 0 (LEAF 8) (LEAF 9)))
          (NODE 0 (NODE 0 (LEAF 10) (NODE 0 (LEAF 12) (LEAF 13))) (LEAF 7))

t3 = NODE 0 (NODE 0 (NODE 0 (LEAF 4) (LEAF 5)) (LEAF 6))
                (NODE 0 (LEAF 8) (LEAF 9))

                
t4 = ListNODE 
 [ ListNODE [ ListLEAF [1,2,3],ListLEAF [4,5],ListNODE([ListLEAF [6], ListLEAF []]) ],    
   ListNODE [], 
   ListLEAF [7,8], 
   ListNODE [ListLEAF [], ListLEAF []] ]

l1 = ListLEAF ["School","-","of","-","Electrical"]
l2 = ListLEAF ["-","Engineering","-"]
l3 = ListLEAF ["and","-","Computer","-"]
l4 = ListLEAF ["Science"]
l5 = ListLEAF ["-WSU"]
n1 = ListNODE [l1,l2]
n2 = ListNODE [n1,l3]
t5 = ListNODE [n2,l4,l5]

tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,
                   TestLabel "Problem 1a - test4 " p1a_test4,
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,
                   TestLabel "Problem 1b - test3 " p1b_test3,
                   TestLabel "Problem 1b - test4 " p1b_test4,
                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3,
                   TestLabel "Problem 2a - test1 " p2a_test1,
                   TestLabel "Problem 2a - test2 " p2a_test2,
                   TestLabel "Problem 2a - test3 " p2a_test3,
                   TestLabel "Problem 2a - test4 " p2a_test4,  
                   TestLabel "Problem 2b - test1 " p2b_test1,
                   TestLabel "Problem 2b - test2 " p2b_test2,
                   TestLabel "Problem 2b - test3 " p2b_test3,  
                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,
                   TestLabel "Problem 3a - test3 " p3a_test3,
                   TestLabel "Problem 3a - test4 " p3a_test4,  
                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,
                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 5 - test1 " p5_test1,
                   TestLabel "Problem 5 - test2 " p5_test2,
                   TestLabel "Problem 5 - test3 " p5_test3
                 ] 
                  

-- shortcut to run the tests
run = runTestTT  tests