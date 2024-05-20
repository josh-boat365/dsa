# You are given a string binarystring consisting of '0's and '1' s, as well as an array of strings requests containing requests of two types:
# requests [i] = "count:
# <index>" - find the number of '0’ s in binarystring before and including the specified 0 - based index .
# requests [i] = "flip" - flip all elements of binarystring, i.e. change every '0' to '1', and
# every '1' to '0’ Return an array answers, where answers [i] contains the answer for the respective count request. For binarystring = "1111010" and
# requests = ["count:4", "count:6", "flip", "count:4", "flip","count: 2"], the output should be solution (binaryString, requests) = [1, 2, 4, 0]


def solution(binaryString, requests):
    n = len(binaryString)
    flipped = False
    answers = []
    for request in requests:
        if requests.startswith('count:'):
            index = requests.split(':')
            index = int(index)
            if not flipped:
                #count '0's in the original string
                count = binaryString[:index + 1].count('o')
            else:
                count = binaryString[:index + 1].count('1')
            answers.append(count)
        elif request == 'flip':
            # Toggle the flipped state
            flipped = not flipped
    return answers

binaryString = "1111010"
requests = ["count:4", "count:6", "flip", "count:4", "flip", "count:2"]
print(solution(binaryString, requests))  
# Output: [1, 2, 4, 0]
                
            