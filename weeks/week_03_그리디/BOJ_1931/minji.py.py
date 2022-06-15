import sys

n = int(input())
timetable = [[0]*2 for i in range(n)] #2차원 시간표 배열
for i in range(n) : #입력 받아서 시작시간과 끝나는 시간 timetable에 저장
  s, f = map(int, sys.stdin.readline().split())
  timetable[i][0]=s
  timetable[i][1]=f

timetable.sort(key=lambda x:(x[1], x[0])) #끝나는 시간 기준으로 정렬
cnt = 1 #수업 개수
end_time = timetable[0][1] #첫번째 시간
for i in range(1, n) :
  if timetable[i][0] >= end_time : #첫번째 수업이 끝난 이후에 시작하는 수업
    cnt+=1
    end_time=timetable[i][1]
print(cnt)