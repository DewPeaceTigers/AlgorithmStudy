import sys
from collections import defaultdict

r,c,k = map(int,input().split())
A=[[0]*100 for _ in range(100)]

for i in range(3):
    temp = list(map(int,input().split()))
    for j in range(3):
        A[i][j]=temp[j]

n,m=3,3
time=0
def countNSort(list):
    counts = []
    for s in set(list):
        if s==0: continue # 0은 세지 않음
        counts.append([s, list.count(s)])
    counts.sort(key=lambda x: (x[1],x[0]))
    return sum(counts, [])
while A[r-1][c-1]!=k and time<101:
    if n>=m:
        longest=0
        for i in range(n):
            counts = countNSort(A[i])
            for j in range(max(len(counts),m)):
                if j>100: break
                if j >= len(counts):A[i][j]=0
                else:A[i][j]=counts[j]
            longest=max(longest,len(counts))
        m=longest
    else:
        longest=0
        for j in range(m):
            temp = [A[i][j] for i in range(m)]
            counts=countNSort(temp)
            for i in range(max(len(counts),n)):
                if i>100: break
                if i >= len(counts): A[i][j]=0
                else : A[i][j]=counts[i]
            longest=max(longest,len(counts))
        n=longest
    for i in range(n):
        t = []
        for j in range(m):
            t.append(A[i][j])
    time+=1
if time==101: print(-1)
else : print(time)




