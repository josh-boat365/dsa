"""_summary_
Finding the absolute value of the maximum difference of two elements in an array given the size of the array    
"""
#Another Alternative 
# def maxdiff(arr, arr_size):
#     max_diff = arr[1] - arr[0]
    
#     for i in range(arr_size):
#         for j in range(i+1 , arr_size):
#             if (arr[j] - arr[i] > max_diff):
#                 max_diff = arr[j] - arr[i]
#                 abs_max_diff = abs(max_diff)
                
#     return abs_max_diff

# arr_size = int(input("Enter size of array: "))
# arr = list(map(int, input("\nEnter numbers: ").strip().split()))[:arr_size]

# print(maxdiff(arr,arr_size))

def max_Diff(arr, arr_size):
    maxDiff = max(arr)
    minDiff = min(arr)
    
    res = abs(maxDiff - minDiff)

    return res

#test case
arr_size = int(input("Enter Size of array: "))
arr = list(map(int, input("Enter array elements: ").strip().split()))[:arr_size]
print("The absolute difference is ",max_Diff(arr, arr_size))