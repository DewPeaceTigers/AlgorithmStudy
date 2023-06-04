import sys
input = sys.stdin.readline

N, M = map(int,input().split())
know = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(M)]

for i in range(M):
    for party in parties:
        if party & know:
            know = know.union(party)
answer = 0
for party in parties:
    if party & know:
        continue
    answer+=1
print(answer)