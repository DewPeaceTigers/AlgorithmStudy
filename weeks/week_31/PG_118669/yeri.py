from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    dic = defaultdict(list)
    intensity = [int(1e9)]*(n+1)
    for i,j,w in paths:
        dic[i].append((w,j))
        dic[j].append((w,i))
    summits = set(summits) # set을 사용하지 않으면 list 내 확인은 O(n)이라 시간초과 난다.
    q=[]
    for gate in gates:
        # 출발 지점에서 시작
        heapq.heappush(q,(0,gate))
        intensity[gate] = 0 # 최단 거리 저장이 아니라 최소 intensity 저장할 것
    while q:
        inten, now = heapq.heappop(q)
        if now in summits or inten > intensity[now]:
            continue
        for w, next in dic[now]:
            best = max(inten,w) # 현재 가장 큰 intensity
            if best < intensity[next]:
                # 더 적나?
                intensity[next] = best
                heapq.heappush(q,(best,next))
    for summit in summits:
        answer.append([summit,intensity[summit]])
    return min(answer, key=lambda x:(x[1],x[0]))