# For an array nums and an integer t (0 ≤ t < nums. length), let's define a cyclic t-shift operation as carrying elements from the end of the array to the beginning.
# For example, applying cyclic t-shift to array nums having values [nums [0],
# nums [1], nums [2], •
# 1]l, where n is the length of the nums [n-
# nums :
# • For t = 0, the cyclic 0-shift will be [nums [0], nums [1], nums [2], •
# •, nums [n - 1]] .
# • For t = 1, the cyclic 1-shift will be [nums [n - 1], nums [0], nums [1], nums [2], • , nums [n
# - 2]] .
# • For t = 2, the cyclic 2-shift will be [nums [n - 2], nums In - 1],
# nums [O], nums [1], nums [2], ..., nums [n - 3]]
# • For t = n-1, the cyclic (n-1)-shift will be [nums [1], nums [2], .., nums [n - 1], nums [0]] .
# For example, the video below presents all cyclic shifts of the array [5, 4, 3,
# For example, the video below presents all cyclic shifts of the array [5, 4, 3,
# 2, 1] :

# Given an array of integers nums, find such t (0 ≤ t < nums. length ) that cyclic t-shift operation turns nums into a reverse sorted array In, n - 1, ...,
# 1] . If there is no such t, return -1.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
# • (nums. 7ength?) will fit within the
# For nums = [1, 4, 2, 3], the output should be

# solution (nums) = -1
# For nums = [3, 2, 1, 5, 4] the output should be

# solution (nums) = 2.




def cyclic_shift(nums, t):
    #Calculate cyclic shits using slicing - this uses slicing to perform the shifts
    return nums[-t:] + nums[:-t]

def find_cyclic_shifts(nums):
    n = len(nums)
    #creating the reserve of the sorted target array
    target = sorted(nums, reverse=True)
    
    for t in range(n):
        if cyclic_shift(nums, t) == target:
            return t
    return -1

#test cases
nums = [5,4,3,2,1]
nums2 = [1,4,2,3]
nums3 = [3,2,1,5,4]
print(find_cyclic_shifts(nums))
print(find_cyclic_shifts(nums3))