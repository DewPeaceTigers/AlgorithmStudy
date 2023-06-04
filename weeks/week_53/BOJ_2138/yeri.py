import sys
input = sys.stdin.readline

N = int(input())
cur = list(map(int,list(input().rstrip())))
dream = list(map(int,list(input().rstrip())))
answer = int(1e9)
# 첫 누르기
now = cur[:]
now[0] = 1-now[0]
now[1] = 1-now[1]
pressO = 1
for i in range(1,N):
    if now[i-1] != dream[i-1]:
        pressO+=1
        for n in range(i-1,i+2):
            if n<N:
                now[n] = 1-now[n]
if now == dream:
    answer = pressO

# 첫 누르지 않기
now = cur[:]
pressX = 0
for i in range(1,N):
    if now[i-1] != dream[i-1]:
        pressX+=1
        for n in range(i-1,i+2):
            if n<N:
                now[n] = 1-now[n]
if now == dream:
    answer = min(answer,pressX)

if answer == int(1e9):
    answer = -1
print(answer)
