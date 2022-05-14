def solution(n):
    for i in range(len(n)):
        if n[i] < n[i+1] < n[i +2]:
            True
        else:
            False
            
n = [0,2,3,7,6]
print(solution(n))
   


           

          