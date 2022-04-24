#finding the fibonacci of a sequence
def fibo(n):
    if n <=1:
      return n
    else:
        return fibo(n-1) + fibo(n-2)
    
print( "The Fibonacci Series of 15 is: ",fibo(15))

#sum elements in an arr
def sumArr(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

arr = [1,2,3,4,5]

print("The sum of the arrray is", sumArr(arr))

#reversing an array
def reverseArr(ar):
    arr = ar[::-1]
    return arr

array = [1,2,3,4,5,6,7,8,9]
output = reverseArr(array)

print("The original array is {0} \n and the reversed array is {1}".format(array, output))

#finding the factorial of a number 
def fact(f):
    if f == 0:
        return 
    if f == 1:
        return f
    else:
        return f * fact(f-1)
    
print("The factorial of 7 is ", fact(2))