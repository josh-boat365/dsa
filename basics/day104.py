from tkinter import N
from numpy import array2string


def sumArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
 
a = [1,2,3,4,5]         
print(sumArr(a))


def compareTriplets(a,b):
    for i in a:
        for j in b:
            if i > j:
                a[i] = a[i] + 1
            elif j > i:
                b[j] = b[j] + 1
            elif i == j:
                0
            else: 
                0
  
   
   
    
 
 
a = [5,6,7]
b = [3,6,10]
# CODe$@2022
print(str(compareTriplets(a,b)))

# def reverseArr(arr):
#         return arr[::-1]

# a = ["cat", "dog", "sheep"]
# print(reverseArr(a))