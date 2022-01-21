import sys
input = sys.stdin.readline

N=int(input())
meetings = [list(map(int,input().split())) for _ in range(N)]

meetings.sort(key=lambda x:(x[1],x[0])) # 종료시간 기준으로 정렬 후 시작시간 기준으로 정렬

room=[meetings[0]] # 가장 빨리 종료하는 애 기준
for i in range(1,len(meetings)):
    isFit=False
    if room[-1][1]<=meetings[i][0]: # 마지막 미팅 종료시간이 현재 미팅 시작시간과 같거나 작을때
        room.append(meetings[i])
print(len(room))