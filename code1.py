"""_summary_
    write a function that takes two integers N and K and an array of N integers as input. Your program should output the index (0-based index) 
    of the array, such that the number of occurences of K before and after that index is the same.
    Returns:
        _type_: _description_ 
        
"""

# n = input()
# k = input()
# arr = [1,5,3]

# print(arr[0])

# if k != arr[0] and k != arr[2]:
#     print(arr[0])
# else:
#     print("none")

def mid_of_k(n,k, arr):
    assert n == len(arr)
    assert k in arr
    begin_index = 0
    end_index = n - 1
    while begin_index <= end_index:
        mid_index = (begin_index + end_index) // 2
        print(f"begin_index: {begin_index}, end_index: {end_index}, mid_index: {mid_index}")
        if arr[:mid_index].count(k) == arr[mid_index+1:].count(k):
            return mid_index
        elif arr[:mid_index].count(k) > arr[mid_index+1:].count(k):
            end_index = mid_index - 1
        elif arr[:mid_index].count(k) < arr[mid_index+1:].count(k):
            begin_index = mid_index + 1
    return "Something is wrong"

arr = [1,5,3]
mid_of_k(3,5,arr)