import sys

T=int(input())

for i in range(T) :
    N=int(input())
    score=[]
    for i in range(N):
        a, b=map(int, sys.stdin.readline().split())
        score.append((a, b))

    score.sort()
    Max=score[0][1]
    count=1
    for i in range(N):
        if Max > score[i][1] :
            count+=1
            Max=score[i][1]

    print(count)
