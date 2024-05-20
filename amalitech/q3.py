# Given an array of positive integers numbers . calculate how many of its elements have an even number of digits.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than 
# 0(numbers. length?) will fit within
# the execution time limit.
# Example
# For numbers = [12, 134, 111, 1111, 10] , the
# output should be solution(numbers) = 3.
# • numbers [0] = 12 has 2 digits, which is an even number.
# • numbers[1] = 134 has 3 digits, which is not an even number.
# • numbers(2] = 111 has 3 digits, which is



def solution(numbers):
    even_numbers_count = 0
    for number in numbers:
        if len(str(number)) % 2 == 0:
            even_numbers_count += 1
            
            
    return even_numbers_count
            
num = [12, 134, 111, 1111, 10]
print(solution(num)) 