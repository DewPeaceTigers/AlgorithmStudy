'''
틀림
import sys
input=sys.stdin.readline

n=int(input())

timetable=[]
dp=[]
sum=0
for i in range(n) :
    time, cost=map(int, input().split())
    if i+time > n : #상담 종료되는 날이 퇴사날 이후이면 넣지x
        timetable.append([0, 0])
        dp.append(0)
    else:
        timetable.append([time, cost])
        dp.append(cost)

#print(timetable)
#print(dp)
for i in range(n) :
    if dp[i]>dp[i+1] :
        dp[i+1]=dp[i]
    if dp[i+timetable[i][0]]<dp[i]+timetable[i][1] :
        dp[i+timetable[i][0]]=dp[i]+timetable[i][1]

print(max(dp))

'''
'''뒤에서 부터 풀면 됨'''
import sys
input=sys.stdin.readline

n=int(input())

times=[]
costs=[]
dp=[0]*(n+1)
for i in range(n) :
    time, cost=map(int, input().split())
    times.append(time)
    costs.append(cost)

for i in range(n-1, -1, -1) :
    if times[i]+i > n :
        dp[i]=dp[i+1]
    else:
        dp[i]=max(costs[i]+dp[i+times[i]], dp[i+1])

print(dp[0])