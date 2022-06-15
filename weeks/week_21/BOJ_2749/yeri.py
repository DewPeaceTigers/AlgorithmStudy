"""
생각했던 풀이
temp1=1
temp2=1

for i in range(3,n+1):
    temp1,temp2 = temp2, (temp1+temp2)%1000000
print(temp2)

이용해야하는 것 : 피사노 주기
- 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게 된다.
- 주기의 길이가 P이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같다
  - N%M == (N%P)%M
- M = 10^k & k>2 -> 주기 : 15*10^(k-1)
"""

import sys

input = sys.stdin.readline

n = int(input())
mod = 1000000
p = mod//10*15
arr = [0]*p
arr[1]=1
for i in range(2,p):
    arr[i]= (arr[i-1]+arr[i-2])%mod

print(arr[n%p])