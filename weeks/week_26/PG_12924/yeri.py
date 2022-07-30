import math
def solution(n):
    cnt=1
    for i in range(1,n+1):
        sum=i
        for j in range(i+1,n+1):
            sum+=j
            if n == sum :
                cnt+=1
                break
            if n < sum:
                break
    return cnt