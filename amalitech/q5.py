# Given an array of integers numbers, construct a new array in the following manner:
#     • The first element of the new array is the first element of numbers;
# • The second element of the new array is the last element of numbers;
# • The third element of the new array is the second element of numbers ;
# • The fourth element of the new array is the second-to-last element of numbers ;
# ..and so on, until the new array contains all elements of
# For numbers = [0, 4, 3, 2,1], the output should be
# solution (numbers) = [0, 1, 4, 2, 31 -
# For numbers = [-5, 4, 0, 3, 2, 2], the output should be
# solution (numbers) = [-5, 2, 4, 2, 0, 31 -

def solution(numbers):
    result = []
    left = 0
    right = len(numbers) - 1
    
    while left<= right:
        if left == right:
            result.append(numbers[left])
        else:
            result.append(numbers[left])
            result.append(numbers[right])
        left += 1
        right -= 1
        
    return result

#example
construct_arr1 =  [0, 4, 3, 2, 1]
construct_arr2 =  [-5, 4, 0, 3, 2, 2]
print(solution(construct_arr1))
print(solution(construct_arr2))


# You are given a string text consisting of unique lowercase
# English words that are divided by spaces.
# Your task is to count the absolute
# difference between the number of
# vowels (which are ‘a’, ‘e’, 'i’, ‘o', and 'u' and the number of consonants in each word. 
# You are to return the array of words in the ascending order of these absolute differences. If the absolute difference is the
# same, sort the words in alphabetical order

# Example 1: For text = "penelope lives in hawaii", the output should be
# solution (text) = ["in", "penelope","lives", "hawaii"].

# You are given an array of integers numbers. Your task is to count the number of distinct pairs (i, j) such that 0 ≤ i < j < numbers.length,
# numbers [i] and numbers [j] have the same number of digits,
# and exactly one of the digits differs between numbers [il
# and numbers [jl.        
# For numbers = [1, 151, 241,
# 1, 9, 22, 351], the output should be solution (numbers) = 3

# You are given a string of digits panel and an array of strings codes
# Each string in the
# codes array consists of digits only and represents a code in the following format: "<index> <pattern>", where both index and pattern should consist of at least one digit. Since there
# are several ways to split the code, let's consider them all in ascending order of index length
# and call them split-cases. For instance, for the code = "1324", the split-cases are:
# • split-case 1: index = "1" and pattern = "324" :
# • split-case 2: index = "13" and pattern = "24" ;
# • split-case 3: index = "132" and pattern = "4").
# For each code in codes and for every split-case of this code, check whether a string pattern is present at the index position in the panel string. Return a string array consisting of results of these checks, where each element is either pattern, if this pattern is present in panel, or otherwise "not found"

# For panel = "2311453915" and codes = ("0211", "639"), the output should be
# solution (panel, codes) = ["not found", "11", "not found", "39", "not
# found" ]

# For a rectangular matrix of integers, a cross is a figure formed by joining one row and one column. 
# A cross is considered to be regular if all the elements in it are equal. A cross is called nearly regular if all of its elements are equal except for, at times, 
# the element in the intersection of the row and the column which form the cross.
# You are given a rectangular matrix of integers matrix. Your task is to return the number of nearly regular crosses within matrix. 
# Note that by definition the regular cross is also considered to be a nearly regular cross.

# matrix=[
# [1, 1, 1, 1],
# [2, 3, 1, 1],
# [1, 1, 1, 0],
# [1, 4, 1, 1]
# ]
# Output should be 2

# You are given an array of integers arr. Consider its elements in pairs: (arr [0], arr [1]), (arr [2], arr[3]) , and so on.
# Arrange the elements in each pair in ascending order. In other words, swap the position of paired elements 
# if the left element is greater than the right one.
# If arr contains an odd number of elements, the last element should be left unchanged.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not 
# worse than 0(arr. length?) will fit within the execution time limit.

# • For arr = [1, 5, 7, 3, 2, 1] , the output should be
# solution (arr) = [1, 5, 3, 7, 1, 2]

# Imagine that you are going fishing at the local pond. The size of the bait must be strictly smaller than the size of the fish for it to catch. Once the fish is caught, it is removed from the pond and cannot be caught again. However, each bait can be used up to 3 times before depletion.
# Given two arrays of fish and baits, where fish[i] corresponds to the size of the ith fish in the pond, and baits [j] corresponds to the size of the jth bait, your task is to return the maximum number of fish you can catch from the pond with the given baits.
# To compute the answer, you need to use each bait to its possible extent, going from the largest bait to the smallest bait. Use each bait to catch the largest fish remaining in the pond and move to the
# next bait if the current bait was used three times or if it is not strictly smaller than the largest remaining fish. When you run out of baits, return the number of caught fish.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
# O(max(fish. length, baits. length)?) will fit within the execution time limit.

# • For Fish - [1, 2, 3] and baits - [1], the output
# should be solution(fish, baits) = 2


# Imagine that you're exploring a mysterious labyrinth in the shape of a rectangular matrix, which contains obstacles and teleports.
# Starting from the upper-left corner, your goal is to reach the lower-right corner by only moving to the right.
# You are given integers n and m representing the dimensions of the labyrinth. You are also given obstacles and teleports,
# which are lists of the cells that contain all the obstacles and teleports, respectively.
# Details about the labyrinth:
# • An obstacle cannot be traversed - you must stop immediately if you reach a cell containing an obstacle.
# • A teleport is a pair of cells (start, end). If you reach the start cell, you immediately move to the end cell.
# • Note that this doesn't work backwards: you cannot teleport from the end cell to the start cell.
# • It is guaranteed that all teleports have unique start cells (i.e. each cell in the labyrinth has one teleport at
# most).
# • It is guaranteed that the end cell for a teleport cannot be a start cell for another teleport. o It is also guaranteed that both the start and end cells of a teleport do not contain obstacles.
# • Any cell that doesn't contain an obstacle or a teleport is considered a free cell, and you can walk through it normally.
# You start at the upper-left corner cell with coordinates (o, 0) , and the goal is to reach the exit located at the cell with coordinates



