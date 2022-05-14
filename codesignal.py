#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.


def product_of_adjacent_elements(array):
     ans = max( a * b for a, b in zip(array, array[1:]))
     
     return ans
 
array = [1,2,3,-4,-5,6,3]

print(product_of_adjacent_elements(array))

#Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.

def area_of_polygon(n):
    area = n**2
    poly1 = n-1
    poly2 = poly1**2
    if n == 1:
        return 1
    else:
        return area + poly2
    
print("The area of a polygon with 2 side: ",area_of_polygon(3))

#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def solution(statues):
    lowest = min(statues)
    highest = max(statues)
    arr = list(range(lowest, highest))
    new = set(arr)
    old = set(statues)
    
    res = len(new - old)
    
    return res


arry = [6,3,2,8]

print(solution(arry))

#Determine whether a string is a palindrome
def isPalindrome(string):
    ans = string[::-1]
    if string == ans:
        return True
    else:
        return False
    
print(isPalindrome("aaa"))

#finding the mean of an array
import math
import numpy as np

a = [[1,2,3,4], 
     [2,3,4,5], 
     [5,6,7,6,]]

# b = np.array(a)
# c = np.mean(b, axis=1)

out_arr = np.arange(3)

d = np.mean(a, axis=1, out=out_arr)

print(d)

def list_mean(p):
    total = 0
    i = 0
    if i < len(p):
        for t in p:
            total = total + p[i]
            i += 1
    return i

    mean = i / len(p)
    return mean

# def arr_mean(n):
#     for i in n:
#         mean = sum(int(n[i])) / len(n[i])
        
#         return mean

# aar = [[1,2,3,4],[23,5],[2,3,4]]   
# print(arr_mean(aar))

def func(lis):
    res= []
    for i in range(1,len(lis)+1):
        if lis[i]==lis[i-1]+1:
            res.append(True)
        else:
            res.append(False)
    return res

    