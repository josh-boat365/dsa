
def solution(n):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            for k in range(i+2, len(n)):
                if n[i] < n[j] < n[k]:
                 True
                else:
                    False
            
n = [0,2,3,7,6]
print(solution(n))


# Using the python you've already learned, write a function that:
# Takes two arguments - the min and max values
# Returns a list of the even numbers between min and max

def findEven(mi, ma):
    evenNumber = []
    while mi <= ma:
        if mi % 2 == 0:
            evenNumber.append(mi)
        mi+=1
    
    return "The list of even numbers are ",evenNumber

print(findEven(1,10))
            
# def get_even_numbers(min, max):
#     even_list = []
#     while min <= max:
#         if min % 2 == 0:
#             even_list.append(min)
#         min += 1
        
#     return even_list        

# print(get_even_numbers(1,10))


i = 0     
while (i < 5):
    i+=1
    print("*"*i)

# No of rows
n = 4

# Loop through rows
for i in range(n):
    
    # Loop to print pattern
    for j in range(n):
        print('*' , end=' ')
    print()