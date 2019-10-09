---------------------------------
-- Example functions to process trees
---------------------------------

import Data.Char

-- Binary tree with data only in leaves
data Tree a = LEAF a | NODE (Tree a) (Tree a)  deriving (Show, Eq)

-- example Tree Int
tree4 = NODE (NODE (LEAF "one") (LEAF "two")) (NODE (LEAF "three") (LEAF "four"))

-- count the number of leaves in the tree
nLeaves :: Num p => Tree a -> p
nLeaves (LEAF _) = 1
nLeaves (NODE t1 t2) = (nLeaves t1) + (nLeaves t2)
-- call nLeaves
l = nLeaves tree4   --returns 4

-- count the number of nodes in the tree
nNodes :: Num p => Tree a -> p
nNodes (LEAF _) = 0
nNodes (NODE t1 t2) =  1 + (nNodes t1) + (nNodes t2)
-- call nNodes
n = nNodes tree4   --returns 3

-- make a copy of the tree
copyTree :: Tree a -> Tree a
copyTree (LEAF x) = LEAF x
copyTree (NODE t1 t2) = NODE (copyTree t1)  (copyTree t2)
-- call copyTree
tree4_copy = copyTree tree4

--tree map
treeMap :: (t -> a) -> Tree t -> Tree a
treeMap op (LEAF x) = LEAF (op x)
treeMap op (NODE t1 t2) = NODE (treeMap op t1)  (treeMap op t2)
-- call treeMap
strUpper s = map toUpper s   --should import Data.Char
tree4_uppercase = treeMap strUpper tree4

-- Pre-Order traversal; returns a list of the leaf values
preOrder :: Tree a -> [a]
preOrder (LEAF x) =  [x]
preOrder (NODE t1 t2) = (preOrder t1) ++ (preOrder t2) 
--call PreOrder
pList = preOrder tree4


--------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
--- Ternary Tree with data in leaves and nodes
data TriTree a = TriLEAF a | TriNODE a (TriTree a) (TriTree a)  (TriTree a)  deriving (Show, Eq)

--example TriTree
tree6 = TriNODE 0 (TriNODE 9 (TriLEAF 1) (TriLEAF 2) (TriLEAF 6) ) (TriNODE 8 (TriLEAF 3) (TriLEAF 4) (TriLEAF 7) ) (TriLEAF 5) 

-- count the number of leaves in the tree
nLeavesTri :: Num p => TriTree a -> p
nLeavesTri (TriLEAF _) = 1
nLeavesTri (TriNODE x t1 t2 t3) = (nLeavesTri t1) + (nLeavesTri t2) + (nLeavesTri t3)
-- call nLeavesTri
ll = nLeavesTri tree6   --returns 7

copyTreeTri :: TriTree a -> TriTree a
copyTreeTri (TriLEAF x) = TriLEAF x
copyTreeTri (TriNODE x t1 t2 t3) = TriNODE x (copyTreeTri t1)  (copyTreeTri t2) (copyTreeTri t3)
-- call nNodesTri
tree6_copy = copyTreeTri tree6   --returns 3

treeMapTri :: (a -> a) -> TriTree a -> TriTree a
treeMapTri op (TriLEAF x) = TriLEAF (op x)
treeMapTri op (TriNODE x t1 t2 t3) = TriNODE (op x) (treeMapTri op t1)  (treeMapTri op t2) (treeMapTri op t3)
-- call treeMapTri
myTriTree = treeMapTri (\x -> x*2) tree6

-- PRE-ORDER traversal; returns a list of the leaf values
preOrderTri :: TriTree a -> [a]
preOrderTri (TriLEAF x) =  [x]
preOrderTri (TriNODE x t1 t2 t3) = [x] ++ (preOrderTri t1) ++ (preOrderTri t2) ++ (preOrderTri t3) 
--call preOrderTri
ptList = preOrderTri tree6