import sys
import re
input = sys.stdin.readline

T = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(T):
    now = input().strip()
    m = p.fullmatch(now)
    if m: print("YES")
    else: print("NO")