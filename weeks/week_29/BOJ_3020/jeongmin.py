import sys

input = sys.stdin.readline

N, H = map(int, input().split())

stalactite = [0]* H # 종유석
stalagmite = [0]* H # 석순
obstacle = [1e9] * (H+1)

for i in range(N):
    h = int(input())

    # 짝수번째 : 석순
    if i%2==0:
        stalagmite[h]+=1

    # 홀수번째 : 종유석
    else:
        stalactite[h]+=1


for i in range(H-2, 0, -1):
    stalagmite[i] += stalagmite[i+1]
    stalactite[i] += stalactite[i+1]

obstacle[1] = stalagmite[1]
obstacle[H] = stalactite[1]

for i in range(2, H):
    obstacle[i] = stalagmite[i]+ stalactite[H+1-i]

m = min(obstacle)
print(m, obstacle.count(m))