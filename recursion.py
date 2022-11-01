# f(n) = n! => n*(n-1)!
# f(5) = 5! => 5*4 + 
# f(3) = 3*2 * 1 = 6
# f(2) = 2 * 1 = 2
# f(1) = 1
# f(0) = 0


def fact(n):
    # Base case: 
    if n == 0:
        return 0
    elif n == 1:
        return n
    #    recursive case 
    else:
        return n * fact(n - 1)

print(fact(8))

# finding the greatest commom divisor 
def gcd(a,b):
    # base case
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b , a%b)
    
print(gcd(6,8))