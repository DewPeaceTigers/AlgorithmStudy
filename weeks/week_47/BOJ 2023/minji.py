'''
시작은 소수 2 3 5 7
'''
import math
from collections import deque

n=int(input())

answer=[]

def isPrime(num) :
    for i in range(2, math.floor(math.sqrt(num))+1) :
        if num%i==0 :
            return False
    return True

def dfs() :
    q=deque([2, 3, 5, 7])
    ans=[]
    while q :
        now=q.popleft()
        if len(str(now)) == n :
            ans.append(now)
            continue
        for i in range(1, 10, 2) :
            tmp=now*10+i
            if isPrime(tmp) :
                q.append(tmp)
    return ans

answer=dfs()
for n in answer:
    print(n)