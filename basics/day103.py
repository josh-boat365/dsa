#Link: Educative.io https://www.educative.io/courses/learn-python-3-from-scratch/xlV10w35oPq
# Some examples of recursive algorithms
# Write a function to reverse an array using recursions

# Reversing array without using recursion
# A = [1,2,3,4,5,6]
# print(A[::-1])

#reversing array using recursion


def reverseArray(arr):
    #Base case
    if len(arr) == 0: #if the array is empty just return the empty array
        return []
    elif len(arr) == 1: # if the size of the array is 1 then return the same array
        return arr
    
    
    #Recursive case
    return [arr[len(arr)-1]] + reverseArray(arr[:len(arr)-1]) # the first part stores the last element of the array and the second part is calling an instance of the function with the last element removed.

A = [1,2,3,4,5,65]
print("Printing an array in a reverse order:..........")
print("Array in orignal form:")
print(A)
print("Array in reversed form:")
print(reverseArray(A))

#Findig the GCD of two numbers
def gcd(a,b):
    #Base case
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        #Recursive Structure
        return gcd(b , a% b)
    

a =  int(input("Enter Num 1: "))
b =  int(input("Enter Num 2: "))
res =gcd(a,b)
print("The Greatest Common Divisor of {0} and {1} is: {2}".format(a, b, res))


#Write a function to replace all -negative integers with 0
currentIndex = 0
#using recursions
def replaceIntWithZero(array, currentIndex):
    if currentIndex < len(array):
        if array[currentIndex] < 0:
            array[currentIndex] = 0
            
        replaceIntWithZero(array, currentIndex + 1)
        
    return

#using iterations
# def replaceIntWithZero(array, currentIndex):
#     while(currentIndex < len(array)):
#         if array[currentIndex] < 0:
#             array[currentIndex] = 0
            
#         currentIndex += 1
        
#testing       
    
arr = [1-2,-3, 4,5,6,-11,-15,-12]
replaceIntWithZero(arr, 0)
print(str(arr))


