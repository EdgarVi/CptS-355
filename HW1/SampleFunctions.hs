-- CptS 355 - Fall 2019 Solution : 08/29/2019

module SampleFunctions
     where

import Data.Char 


{-
extract value from list of tuples:
[("parentA", ["James", "Jack"]),
("parentB", ["Myra"]),
("parentC", ["Will", "Ben", "Even"])]
-}
-- function to return a list of parents that have 2 or more children
getParent [] = []
getParent((p, kids):xs) = if (length kids) >= 2 then p:(getParent xs)
                          else (getParent xs)

-- nth element

nthElement [] n = error "nthElement': The input list is too short."
nthElement (x:xs) 1 = x
nthElement (x:xs) n = (nthElement xs (n-1))


-- allSquares
allSquares :: Num a => [a] -> [a]
allSquares [] = []
allSquares (x : xs) = x * x : allSquares xs
                   
-- Check if a list is empty 
isNull :: [a] -> Bool
isNull [] = True
isNull (x:xs) = False


-- length of a list
length' :: [a] -> Int
length' [] = 0
length' (x:xs) = 1 + (length xs)

myChar = nthElement "CptS355-Assignment1" 5

main = do print ( nthElement [1,2,3,4,5] 4)
          print ( allSquares [1,2,3,4,5] )
          print ( length [1,2,3,4,5] )
          print (myChar)

-- 5. isPalindrome
isPalindrome :: [Char] -> Bool
isPalindrome [] = True
isPalindrome st = simplePalindrome (disregard st)

simplePalindrome :: String -> Bool
simplePalindrome st = (reverse' st == st)

-- from lecture slides
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = (reverse' xs) ++ [x]

-- trim string and disregard punctuation
disregard :: String -> String
disregard st = remove (change st)

remove :: String -> String
remove [] = []
remove (a:st)
    | notPunctuation a = a:(remove st)   
    | otherwise = remove st

notPunctuation :: Char -> Bool
notPunctuation ch = isLetter ch || isDigit ch

isLetter :: Char -> Bool
isLetter ch = 'A' <= ch && ch <= 'z'

-- converts string to lowercase
change :: String -> String
change [] = []
change (a:st) = (convert a ):(change st)

-- converts character to lowercase
convert :: Char -> Char
convert ch 
    | isCap ch = toEnum (fromEnum ch + offset)
    | otherwise = ch
    where
    offset = fromEnum 'a' - fromEnum 'A'

isCap :: Char -> Bool
isCap ch = 'A' <= ch && ch <= 'Z'

isDigit :: Char -> Bool
isDigit ch = '0' <= ch && ch <= '9'


-- prereqFor
prereqFor :: Eq t => [(a, [t])] -> t -> [a]
prereqFor [] _ = []
prereqFor coursesList target = (findCourses coursesList target [])

findCourses :: Eq t => [(a, [t])] -> t -> [a] -> [a]
findCourses [] target accum = accum
findCourses (x:xs) target accum
    | (exists target (snd x)) == True = (findCourses xs target ((fst x):accum))
    | (exists target (snd x)) == False = (findCourses xs target accum)

-- 5. isPalindrome
isPalindrome :: [Char] -> Bool
isPalindrome [] = True
isPalindrome str = sanitizeStr str == reverse' (sanitizeStr str)
 
-- driver function
sanitizeStr :: [Char] -> [Char]
sanitizeStr [] = []
sanitizeStr str = strToUpper (strTrim str)

-- trim spaces from string
strTrim :: [Char] -> [Char]
strTrim [] = []
strTrim (s:strs)
    | isLetter s == True = s:(strTrim strs)
    | otherwise = strTrim strs

-- check if char is letter
isLetter :: Char -> Bool
isLetter ch = 'A' <= ch && ch <= 'z'

-- convert string to upper, from lecture slides
-- toUpper converts only a character to upper
strToUpper :: [Char] -> [Char]
strToUpper [] = []
strToUpper (s:strs) = (toUpper s):(strToUpper strs)


-- from lecture slides
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = (reverse' xs) ++ [x]

-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]
groupSumtoN _ [] = [[]]
groupSumtoN n xlist = groupSumtoNHelper n xlist []

groupSumtoNHelper :: (Ord a, Num a) => a -> [a] -> [a] -> [[a]]
groupSumtoNHelper n [] acc = [acc]
groupSumtoNHelper n (x:xs) acc
    | (addup 0 acc) + x > n = (reverse acc):(groupSumtoNHelper n xs [x])
    | otherwise = (groupSumtoNHelper n xs (x:acc))
