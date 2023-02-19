import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())
known = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M): # for kn in known => 으로만 함
    # 모든 파티가 확인 가능하도록
    for party in parties:
        if party & known:
            known = known.union(party)
answer=0
for party in parties:
    if party & known:
        continue
    answer+=1
print(answer)
