"""_title_
    maximun subarray sum (kadane's algorithm)
    
    _question_
    given an array x[] of n integers, write a program to  find the maximum sum of a subarray among all subarrays.
    
    _summary_
    a subarray of array x[] is a contiguous segment of elements from x[i] through x[j], where 0 < =i < = j < = n.
    if the array contains all non-negative numbers, the maximum subarray sum would be the sum if the entire array.
    several different sub-arrays may have the same max sum but we need to just return the value of the max subarray sum.
  
"""

def getMaxSubarraySum(arr, n):
    maxSumEnding= [0]*n
    maxSumEnding[0] = arr[0]

    for i in range(1, n):
        if maxSumEnding[i-1] > 0:
            maxSumEnding[i] = arr[i] + maxSumEnding[i -1]
        else:
            maxSumEnding[i] = arr[i]
    maxSubarraySum = 0
    for i in range(0, n):
        maxSubarraySum = max(maxSubarraySum, maxSumEnding[i])
    return maxSubarraySum


# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# n = len(arr)
# max_sum = getMaxSubarraySum(arr, n)
# print("Maximum contiguous sum is ", max_sum)


# what is the difference between the two program codes

# link: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# def largest_sum_contiguous_subarray(a):
    # max_so_far = 0
    # max_ending_here = 0

    # for i in range(0, len(a)):
    #     max_ending_here = max_ending_here + a[i]
    #     if max_ending_here < 0:
    #         max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
    #     elif (max_so_far < max_ending_here):
    #         max_so_far = max_ending_here

    # return max_so_far


# Driver program to check the above function
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# print("Maximum contiguous sum is", largest_sum_contiguous_subarray(a))


#simplified solution 
def maxSubarraySum( arr, n):
    #this is the maximum sum of any subarray in the given aray 'arr'
    maxSum_of_Subarray = 0
    #this is the maximum sum of the subarray which is ending at the current element.
    maxSum_of_Subarray_Ending = 0
    
    for i in range(0, n):
        maxSum_of_Subarray_Ending += arr[i]
        if maxSum_of_Subarray_Ending < 0:
            maxSum_of_Subarray_Ending = 0
        elif (maxSum_of_Subarray < maxSum_of_Subarray_Ending):
            maxSum_of_Subarray = maxSum_of_Subarray_Ending
    return maxSum_of_Subarray

arr = [-2, -3, 4, -1, 7, 1, 5, -3]
n = len(arr)
max_sum = maxSubarraySum(arr, n)
print("Maximum contiguous sum is ", max_sum)