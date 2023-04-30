import sys
import re

input=sys.stdin.readline

t=int(input())
p=re.compile('(100+1+|01)+')

for _ in range(t) :
    s=input().rstrip()
    m=p.fullmatch(s)
    if m :
        print("YES")
    else:
        print("NO")