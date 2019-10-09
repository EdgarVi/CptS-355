-- CptS 355 - Fall 2019 Assignment 1
-- Edgar Villasenor, WSU ID: 11536698

module HW1
     where

import Data.Char (toUpper)

-- 1. exists
exists :: Eq t => t -> [t] -> Bool
exists searchVal myList
     | length myList == 0 = False 
     | head myList == searchVal = True
     | head myList /= searchVal = exists searchVal (tail myList)
{-
Follow up question:

This is because only types that support equality testing can be passed
as arguments to the function. Since "==" and "/=" are used in the
function definition, it is implied the paramters will be compared
for equality
-}

-- 2. listUnion
listUnion :: Eq a => [a] -> [a] -> [a]
listUnion [] [] = []
listUnion listx listy = 
    let listUnion' [] res = res
        listUnion' (y:ys) res
            | (exists y res) == True = (listUnion' ys res)
            | otherwise = (listUnion' ys (y:res)) 
    in (listUnion' listy (listUnion' listx [])) 

-- 3. replace
replace :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2] 
replace _ _ [] = [] -- list is empty, return empty
replace 0 v (x:xs) = [v] ++ xs
replace n v (x:xs) = [x] ++ (replace (n - 1) v xs)


-- 4. prereqFor
prereqFor :: Eq t => [(a, [t])] -> t -> [a]
prereqFor [] _ = []
prereqFor coursesList target = 
    let prereqFor' [] target accum = accum
        prereqFor' (x:xs) target accum
            | (exists target (snd x)) == True = (prereqFor' xs target ((fst x):accum))
            | (exists target (snd x)) == False = (prereqFor' xs target accum)
    in (prereqFor' coursesList target [])

-- 5. isPalindrome
isPalindrome :: [Char] -> Bool
isPalindrome [] = True
isPalindrome str = sanitizeStr str == reverse (sanitizeStr str)
     where sanitizeStr [] = []
           sanitizeStr str = strToUpper (strTrim str)
           strTrim [] = [] -- trim spaces from string
           strTrim (s:strs)
               | isLetter s == True = s:(strTrim strs)
               | otherwise = strTrim strs
           isLetter ch = 'A' <= ch && ch <= 'z' -- check if char is letter
           strToUpper [] = []
           strToUpper (s:strs) = (toUpper s):(strToUpper strs)
           
-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]
groupSumtoN _ [] = [[]]
groupSumtoN n xlist = groupSumtoN' n xlist []
    where groupSumtoN' n [] acc = [acc]
          groupSumtoN' n (x:xs) acc
              | (addup 0 acc) + x > n = (reverse acc):(groupSumtoN' n xs [x])
              | otherwise = (groupSumtoN' n xs (x:acc))
          addup accum [] = accum -- list empty, addup bound to accum
          addup accum (x:xs) = (addup (accum + x) xs) -- pass in accum + x's value and the list sans x