"""
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""
def minMaxSum(arr):
    # arr = list(map(int, input().strip().split()))
    #arrange array elements in order from ascending to descending order
    arr.sort()
    #sum array elements from the first index to the last but one index of the array
    x = sum(arr[0:-1])
    #sum array elements from the second index to the last index of the array
    y = sum(arr[1:])
    #return result 
    print(x,y)
    #one line code 
    # print(sum(sorted(arr[0:-1])), sum(sorted(arr[1:])))

arr = [1,2,3,4,5]
minMaxSum(arr)
# print(type(minMaxSum(arr)))
