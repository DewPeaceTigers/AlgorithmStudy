import sys
input = sys.stdin.readline

N,M = map(int,input().split())

min_p = 1001
min_a = 1001
for i in range(M):
    temp= list(map(int,input().split()))
    min_p = min(min_p,temp[0])
    min_a = min(min_a,temp[1])

p = N // 6
a = N % 6
p_price=0
a_price=0

if min_p < min_a * a:
    # 세트로 몽땅 사는게 나을 경우
    p+=1
    p_price = min_p
elif min_p > min_a * 6:
    # 낱개로 사는 게 나을 경우
    a_price=min_a
    a = N
else:
    p_price,a_price = min_p, min_a

print(p*p_price+a*a_price)
