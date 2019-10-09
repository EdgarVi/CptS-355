module HWEx
    where

append :: [a] -> [a] -> [a]
append [] list = list
append(x:xs) list = x:(append xs list)

natSum :: (Num a, Ord a) => a -> a
natSum 0 = 0
natSum n | n > 0 = n + natSum (n - 1)
         | otherwise = error "n is negative"  

{-
remember, : appends an item to the head of a list
so what are we doing here?
Using the : operator, we use pattern matching to decompose
lists into their first element and the rest of the list

-}
length' :: [a] -> Int
length' [] = 0
length' (x:xs) = 1 + (length' xs) -- think what's happening here


-- here is a very intuitive example of pattern matching
last' :: [a] -> a
last' [] = error "list is empty" -- empty list
last' [x] = x -- only one element in list, return it
last' (x:xs) = (last xs) -- return everything in the list except for the first element

nthElement [] n = error "List is too short"
nthElement (x:xs) 1 = x -- once n == 1, return x
nthElement (x:xs) n = (nthElement xs (n - 1)) -- recurse, xs is the list sans the first element

addup :: Num p => [p] -> p
addup [] = 0
addup (x:xs) = x + (addup xs) -- add x's value to addup(list sans x)

-- a bit messy but you need to pass in 0 when calling addup2
addup2 :: Num p => p -> [p] -> p
addup2 accum [] = accum -- list empty, addup2 bound to accum
addup2 accum (x:xs) = (addup2 (accum + x) xs) -- pass in accum + x's value and the list sans x
{-
why does having an accum make the function tail recursive? 
Apperently all languages are like this and it's something the compiler
optimizes for
-}

{-
groupSumtoNHelper _ [] acc result = ((reverse' acc):result)
groupSumtoNHelper n (x:xs) acc result
    | (addup 0 acc) + x > n = (groupSumtoNHelper n xs [] ((reverse' acc):result))
    | otherwise = (groupSumtoNHelper n xs (x:acc) result)
-}
{-groupSumtoNHelper _ [] acc result = ((reverse' acc):result)
groupSumtoNHelper n (x:xs) acc result
    | (addup 0 acc) + x <= n = (groupSumtoNHelper n xs [] ((reverse' acc):result))
    | otherwise = (groupSumtoNHelper n xs (x:acc) result)
-}

-- 4. prereqFor
{-
extract value from list of tuples:
[("parentA", ["James", "Jack"]),
("parentB", ["Myra"]),
("parentC", ["Will", "Ben", "Even"])]

-- function to return a list of parents that have 2 or more children
getParent [] = []
getParent((p, kids):xs) = if (length kids) >= 2 then p:(getParent xs)
                          else (getParent xs)

in preReqFor we're passing in:
    1) a list of tuples
    where the first value is a string and the second value
    is a list of strings
    2) a course name 
and we want to return:
    a list of courses for which the string is a prereq for

in imperative languages, this would be a piece if cake:
    for each tuple, check the second val for the target,
    if target found, add the first tuple element

note: we can use == directly on lists/strings
-}

-- 6. groupSumtoN
{-
def groupSumtoN(n, i):
	result = []
	acc = []
	for x in i:
		if sum(acc)+x > n: # acc is full
			result = cons(reverse(acc), result)
			acc = []
		else:
			acc = cons(x, acc)
	result = cons(reverse(acc), result)
return reverse(result)

-}

-- ++ is list append
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = (reverse' xs) ++ [x]

