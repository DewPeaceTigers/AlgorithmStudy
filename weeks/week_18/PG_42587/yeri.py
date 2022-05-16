from collections import deque
def solution(priorities, location):
    p = deque([[priorities[i],i] for i in range(len(priorities))])
    cnt=0
    while p:
        front, idx = p[0]
        if front!=max(p,key=lambda x:x[0])[0]: # 가장 큰 애인지 확인하면 된다.
            p.append(p.popleft())
        else:
            p.popleft()
            cnt+=1
            if idx==location: break
    return cnt