
from math import gcd

n=int(input())
trees=[int(input()) for _ in range(n)]
distances=[]

for i in range(1, n) :
    distances.append(abs(trees[i]-trees[i-1])) #나무들 사이 거리

tmp=distances[0]   
for  distance in distances: #최대공약수 찾기
    tmp=gcd(tmp, distance)

answer=(max(trees)-min(trees))//tmp+1 #최대공약수를 기준으로 세워져야하는 나무
print(answer-len(trees)) #세워져야하는 나무-이미 세워진 나무