from collections import deque
N=int(input())
q=deque([i for i in range(1,N+1)])
cnt=0
while(len(q)!=1):
    cnt+=1
    front = q.popleft()
    if cnt%2==0: # 짝수
        q.append(front)
print(q[0])