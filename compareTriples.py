"""_summary_
This is a program to compare two arrays and determine if say Alice and Bob are having a test to check who had the greatest score in a particular test
if alice[0] > Bob[0] alice scores 1 point or 0 if otherwise
if Alice[1] >  Bob[2] alice scores 1 point or 0 if otherwise
if Alice[2] > Bob[2] alice scores 1 point or 0 if otherwise
if Alice[i] == Bob[i] return 0
"""

def comapreTriples(a,b):
    result = {'alice':0, 'bob':0}
    for x, y in zip(a,b):
        if x > y:
            result['alice']+=1
        elif y > x:
            result['bob']+=1
            
    return result

#Test case
a = [1,23,45]
b = [9, 8, 50]

print(comapreTriples(a,b))