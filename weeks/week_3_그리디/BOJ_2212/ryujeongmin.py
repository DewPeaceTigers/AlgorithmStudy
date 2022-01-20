''' [풀이]
붙어있는 센서마다 거리 차를 구한 후 가장 큰 것을 기준으로 분류를 한다.
내림차순으로 정렬하여 가장 큰 k-1개를 제외한 나머지 거리들의 합 구하기
'''

import sys
input = sys.stdin.readline

# 센서의 개수 N(1 ≤ N ≤ 10,000) 입력
N = int(input())
# 집중국의 개수 K(1 ≤ K ≤ 1000) 입력
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(N-1):
    dist.append(sensor[i+1] - sensor[i])
# 거리 내림차순 정렬    
dist.sort(reverse=True)
    
print(sum(dist[K-1:]))