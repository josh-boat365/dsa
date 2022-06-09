# Finding the permutations of a number and compare with another set of numbers

int1 = str(73125052137)
int2 = str(12537073521)

str1 = sorted(str(int1))
str2 = sorted(str(int2))

sort1 = " ".join(str1)
sort2 = " ".join(str2)

#comparing sorted strings
if sort1 == int2:
    print("Yes")
else:
    print("No")


#Finding the absolute value of the maximum difference of two elements in an array given the size of the array     

def maxdiff(arr, arr_size):
    # arr_size = int(input("Enter size of array: "))
    # arr = list(map(int, input("\nEnter numbers: ").strip().split()))[:arr_size]
    max_diff = arr[1] - arr[0]
    
    for i in range(arr_size):
        for j in range(i+1 , arr_size):
            if (arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]
                abs_max_diff = abs(max_diff)
                
    return abs_max_diff

arr_size = int(input("Enter size of array: "))
arr = list(map(int, input("\nEnter numbers: ").strip().split()))[:arr_size]

print(maxdiff(arr,arr_size))

# arr = [1.6,2.7,3]
# arr_size = len(arr) 
# ans = maxdiff(arr, arr_size)

# print(abs(ans))

# get input of 10 elements and store in a array using python
# n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
# print(a)