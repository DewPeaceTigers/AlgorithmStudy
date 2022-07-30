""" 유클리드 호제법!"""
import sys

input = sys.stdin.readline

N = int(input())

dist = []
x1 = int(input())
for _ in range(N-1):
    x2 = int(input())
    dist.append(x2-x1)
    x1 = x2


# 최대 공약수 구하기
def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a


g = dist[0]
for i in range(1, N-1):
    g = gcd(g, dist[i])

answer = 0
for d in dist:
    answer += d//g-1
print(answer)