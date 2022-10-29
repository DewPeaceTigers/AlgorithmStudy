'''
내림차순으로 하면 50%에서 틀림
'''
import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t) :
    n, m=map(int, input().split())
    wants=[list(map(int, input().split())) for _ in range(m)]
    books=[0]*(n+1)
    #wants.sort(key=lambda x:(-x[1], -x[0]))
    wants.sort(key=lambda x:(-x[1], -x[0]))
    ans=0
    for want in wants :
        for i in range(want[0], want[1]+1):
        #for i in range(want[1], want[0]-1, -1):
            if books[i]==0 :
                ans+=1
                books[i]=1
                break
    print(ans)

