'''
예외 처리 잘 찾아야 함
작은 것을 기준으로 해야 함
'''
import sys
input = sys.stdin.readline
t= int(input())

for _ in range(t):
    m,n,x,y=map(int,input().split())

    if m==1 or n==1:
        print(max(x,y))
        continue
    if x==y and x==1:
        print(1)
        continue
    else:
        left=[]
        small=min(x,y)
        interval = m if small==x else n
        firstLeft= n if small==x else m
        cnt=0
        tmp=small
        left=[tmp]
        foundFlag=False
        while True:
            if tmp == small and cnt!=0:
                break
            if tmp==max(x,y):
                foundFlag=True
                break
            tmp=(tmp+interval)%firstLeft
            tmp=tmp if tmp!=0 else firstLeft
            left.append(tmp)
            cnt+=1
    if not foundFlag: print(-1)
    else: print(cnt*interval+small)