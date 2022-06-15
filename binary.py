# from turtle import right


# def reverseBinaryTree(tree):
#     if tree:
#         left = tree.left
#         right = tree.right
#         tree.left = left
#         tree.right = right
#     reverseBinaryTree(tree.left)
#     reverseBinaryTree(tree.right)






def solve(a0, a1, a2, b0, b1, b2):
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    score = [0, 0]
    for a, b in zip(alice, bob):
        if a > b:
            score[0]+= 1
        elif b > a:
            score[1]+=1
    return score

def compareTriplets(a,b):
    res = [0,0]
    for x, y in zip(a,b):
        if x > y:
            res[0]+=1
        elif y > x:
            res[1]+=1
    return res

def solution(a,b):
    result = [0,0]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] > b[j]:
                result[0]+=1
            elif b[j] > a[i]:
                result[1]+=1
        return result
                

a = [5,6,7]
b = [6,8,9]

print(solution(a,b))

import random 

rand = random.randint(0,10)
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Guess a number between 0 and 9\n"))
    guess_count +=1
    if guess > rand:
        print("Your Guess is too high")
    elif guess < rand:
        print("Your guess is too low")
    elif guess == rand:
        print("Hurray you guessed it right")
        break
        
    if guess_count == 3:
        print("Sorry _(0*0)_ Game Over")
        break
    else:
        print("try again")
    
    