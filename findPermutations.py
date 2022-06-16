"""_summary_
        Finding the permutations of a number and compare with another set of numbers and print yes if they are the same
"""


a = [73125052137]
b = a[::-1]
x = sorted(str(a))
y = sorted(str(b))

m = " ".join(x)
n = " ".join(y)

if m == n:
    print("Yes")
else:
    print("NO")
        
        