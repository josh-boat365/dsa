# Resursion
#1
# Suppose you are standing in a queue of people. How many people are directly behind you in the line?
# Rules:
# 1 - One person ca see the person standing directly in front and behind. so one can't just look back and count
# 2- Each person is allowed to ask questions from the person standing in front or behid. How ca we solve this problem recursively?

# Solution
# 1 - You can look and see if there is a person there. if not, then you can return the answer "0". if there is a pserson, repeat this step, and wait for a response from the person standing behind
# 2 - Once a person recieves a response, they add 1 for the person behind them and respond to the person that asked them or the person standing in front of them.

# Algorithm:

# int peopleCount( Person currPerson):
#     if (noOneBehind(currPerson)){
#         return 0
#     }else{
#         Person personBehind = currPerson.getBehind()
#         return peopleCount(personBehind) + 1
#     }
# 🧵 😁🚀💯

# Recursive Pseudocode of nth Factorial
def  fact( n):
    #Base case 
    if n == 0:
        return  
    elif n == 1:
        return n
    
    return n * fact(n-1)
    

print(fact(3))

alist = [5,10,15,25]

print(alist[:])
print(alist[::-1])
print(alist[::-2])

