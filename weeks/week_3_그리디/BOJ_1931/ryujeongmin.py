''' [풀이]
최대 사용할 수 있는 회의의 최대 개수
- 끝나는 시간을 기준으로 오름차순 정렬
- 끝나는 시간이 같을 때는 시작 시간 기준으로 오름차순 정렬
'''

import sys
input = sys.stdin.readline

# 회의의 수 N(1 ≤ N ≤ 100,000) 입력
N = int(input())

info=[]
# 각 회의의 정보 (시작 시간, 끝나는 시간) 입력
for _ in range(N):
  info.append(list(map(int, input().split())))

# 끝나는 시간을 기준으로 오름차순 정렬, 
# 끝나는 시간이 같을 때는 시작 시간 기준으로 오름차순 정렬 
info.sort(key=lambda x : (x[1], x[0])) 
# info.sort(key=lambda x : (x[1])) # 이렇게 한 경우 틀림!

cnt=0 # 회의 개수
end_time =0 # 이전 회의 끝나는 시간

for time in info:
  # 이전 회의 끝나는 시간 <= 해당 회의 시작 시간
  if end_time<=time[0]:
    end_time=time[1]
    cnt+=1

# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
print(cnt)