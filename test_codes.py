#finding the factorial
def fact(n):
    if n == 0:
        return
    elif n == 1:
        return n
    else:
        return n * fact(n -1)

#test codes
print("Finding the factotrial.........")
print("The factorial of the 3 is = ", fact(3))

#finding the fibonacci of a number
def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
print("\nFinding the Fibonacci........")
print("The fibonacci on 7 is ", fibo(7))

#reverse an array
def reverseArray(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        return [arr[len(arr)-1]] + reverseArray(arr[:len(arr)-1])

arr = [1,2,34,590,-3,-5]
print("\nReversing a given array.......")
print(f"The reverse of the {0} is ...",arr)
print("The reversed array is ", reverseArray(arr))

a = [2,4,6]
b = [3,5,6]

print(zip(a,b))