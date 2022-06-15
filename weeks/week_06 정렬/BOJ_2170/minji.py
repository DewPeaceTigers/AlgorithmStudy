'''
선분의 경우
1. 포함되는 경우
2. 서로 연결이 안되어있는 경우
3. 서로 연결되어있는 경우
'''
import sys
n=int(input())
line=[]
for i in range(n) :
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort()
length=0
start, end=line[0][0], line[0][1]
for i in range(1, n) :
    if end>line[i][0] : #선분이 겹치는 경우
        end=max(end, line[i][1])
    else : #선분이 따로 있는 경우
        length+=end-start
        start, end=line[i][0], line[i][1]
length+=end-start
print(length)