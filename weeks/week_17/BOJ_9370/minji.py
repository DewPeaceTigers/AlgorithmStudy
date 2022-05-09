'''
출발-h-g-도착
출발-g-h-도착

'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [100000000 for i in range(n + 1)]
    dp[start] = 0
    while heap:
        we, nu = heappop(heap)
        for ne, nw in s[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heappush(heap, [wei, ne])
    return dp

T= int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    start, g, h = map(int, input().split())
    s = [[] for i in range(n + 1)]
    de = []
    for j in range(m):
        a, b, d = map(int, input().split())
        s[a].append([b, d])
        s[b].append([a, d])
    for k in range(t):
        de.append(int(input()))
    start_ = dijkstra(start)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    an = []
    for l in de:
        if start_[g] + g_[h] + h_[l] == start_[l] or start_[h] + h_[g] + g_[l] == start_[l]:
            an.append(l)
    an.sort()
    for f in an:
        print(f, end=' ')
    print()