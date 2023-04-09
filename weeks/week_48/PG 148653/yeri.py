from collections import deque
def solution(storey):
    answer = 0
    q = deque([[storey,0]])
    limit = storey*2
    visit = [int(1e9)]*limit
    visit[storey] = 0
    while q:
        now, cnt = q.popleft()
        print(now,cnt)
        if now == 0:
            answer = cnt
            break
        n = 1
        while True:
            if now + n < limit and visit[now+n] > cnt+1:
                q.append([now+n,cnt+1])
                visit[now+n] = cnt+1
            if now - n >=0 :
                if visit[now-n] > cnt+1:
                    q.append([now-n,cnt+1])
                    visit[now-n] = cnt +1
            else:
                break
            n*=10
    print(visit)
    return answer
print(solution(2554))