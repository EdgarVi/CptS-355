-- CptS 355 - Fall 2019 Assignment 2
-- Edgar Villasenor WSU ID: 11536698

module HW2
     where


{- 1-  merge2 & merge2Tail & mergeN - 22% -}

--merge2
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 xs [] = xs
merge2 [] ys = ys
merge2 (x:xs) (y:ys)
    | y < x = y:(merge2 (x:xs) ys)
    | otherwise = x:(merge2 xs (y:ys))

--merge2Tail
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail xs ys = merge2TailHelper xs ys []
    where merge2TailHelper xs [] accum = (revAppend accum xs)
          merge2TailHelper [] ys accum = (revAppend accum ys)
          merge2TailHelper (x:xs) (y:ys) accum
              | y < x = (merge2TailHelper (x:xs) ys (y:accum))
              | otherwise = (merge2TailHelper xs (y:ys) (x:accum))
          revAppend [] acc = acc
          revAppend (x:xs) acc = revAppend xs (x:acc)

--mergeN
mergeN :: (Foldable t, Ord a) => t [a] -> [a]
mergeN iL = foldr merge2 [] iL

{- 2 - getInRange & countInRange - 18% -}

--getInRange
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange _ _ [] = []
getInRange v1 v2 iL = filter inRange iL
    where inRange i
              | i > v1 && i < v2 = True
              | otherwise = False     

--countInRange 
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange _ _ [] =  0
countInRange v1 v2 lol = addUp (map xInRange lol)
    where xInRange iL = length (filter xInRange' iL)
          xInRange' i
              | i > v1 && i < v2 = True
              | otherwise = False
          addUp ls = foldr (+) 0 ls

{- 3 -  addLengths & addAllLengths - 18% -}

data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int
                   deriving (Show, Read, Eq)

-- parametrized data constructor
imperialLength (INCH x) = fromIntegral(x)
imperialLength (FOOT x) = fromIntegral(x) * 12
imperialLength (YARD x) = fromIntegral(x) * 36

-- addLengths 
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths l1 l2 = INCH((imperialLength l1) + (imperialLength l2))

-- addAllLengths
addAllLengths :: [[LengthUnit]] -> LengthUnit
addAllLengths ls = foldr addLengths (INCH 0) (concat ls)

{-4 - sumTree and createSumTree - 22%-}

data Tree a = LEAF a | NODE a  (Tree a)  (Tree a) 
              deriving (Show, Read, Eq)
--sumTree
sumTree :: Num p => Tree p -> p
sumTree myTree = addUp (preOrder myTree)
    where preOrder (LEAF x) = [x]
          preOrder (NODE _ t1 t2) = (preOrder t1) ++ (preOrder t2)
          addUp ls = foldr (+) 0 ls

--createSumTree
createSumTree :: Num a => Tree a -> Tree a
createSumTree (LEAF v) = LEAF v
createSumTree (NODE v1 left right) = NODE(sumTree left + sumTree right) (createSumTree left) (createSumTree right)


{-5 - foldListTree - 20%-}
data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
                  deriving (Show, Read, Eq)

foldListTree :: (a -> a -> a) -> a -> ListTree a -> a
foldListTree f base t = traverseListTree t
    where traverseListTree (ListLEAF tlf) = foldr f base tlf
          traverseListTree (ListNODE tnd) = foldr f base (map traverseListTree tnd)

{- 6- Create two tree values :  Tree Integer  and  listTree a ;  Both trees should have at least 3 levels. -}
-- trees defined in the HW2SampleTests.hs file so they can be used in tests
{-
--Tree Integer
myTree = NODE 50
          (NODE 25 (NODE 20 (NODE 40 (LEAF 1) (LEAF 8)) (NODE 21 (LEAF 21) (LEAF 33))) (NODE 4 (LEAF 11)(LEAF 99)))
          (NODE 75 (NODE 60 (NODE 1929 (LEAF 909)(LEAF 202))(NODE 333 (LEAF 98)(LEAF 1997))) (NODE 85 (LEAF 1001)(LEAF 2009)))

-- List Tree
leaf1 = ListLEAF ["The","-","quick","-","brown"]
leaf2 = ListLEAF ["-","fox","-"]
leaf3 = ListLEAF ["jumped","-","over","-"]
leaf4 = ListLEAF ["the"]
leaf5 = ListLEAF ["-", "lazy", "-", "dog"]
leaf6 = ListLEAF ["-", "edgar", "-", "is", "-", "the", "bee's", "-", "knees!"]


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
-}