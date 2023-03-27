import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
liqs = list(map(int,input().split()))
liqs.sort()

l = 0
r = len(liqs)-1

min_answer = abs(liqs[l]+liqs[r])
m_l = l
m_r = r
while l<r:
    added = liqs[l]+liqs[r]
    if min_answer >= abs(added):
        m_l = liqs[l]
        m_r = liqs[r]
        min_answer = abs(added)
        if min_answer==0:
            break
    if added > 0:
        r-=1
    else :
        l+=1
print(m_l,m_r)