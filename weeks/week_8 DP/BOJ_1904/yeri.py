"""
1이나 0을 n-1과 n-2일 때 숫자들에 적절히 더해주면 n이 구성이 된다.
"""
import sys
input = sys.stdin.readline

n = int(input())
e1,e2=1,2
for i in range(2,n):
    e1,e2=e2,(e1+e2)%15746

print(e2 if n!=1 else 1)