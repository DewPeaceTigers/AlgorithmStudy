import sys

input = sys.stdin.readline

N = int(input())

current = list(map(int, list(input().rstrip())))
target = list(map(int, list(input().rstrip())))

# 원하는 상태를 만들기 위해 스위치를 눌러야 하는 최소 횟수
result = 1e9

# 경우 1) 첫번째 스위치를 안 킨 경우
status = [*current]
push_cnt = 0
# 만들고자 하는 상태와 현재 상태 비교
for i in range(1, N):
    # i-1번 전구의 상태가 다르면 i번 스위치 켜기
    if status[i-1] != target[i-1]:
        push_cnt += 1

        # 전구 상태 변경
        # current[i+1] = 1 if current[i+1]==0 else 0
        status[i] = int(status[i] == 0)

        if i < N-1:
            status[i+1] = int(status[i+1] == 0)
# N번째 전구 상태 확인
if status[N-1] == target[N-1]:
    result = push_cnt

# 경우 2) 첫번째 스위치를 킨 경우
status = current
status[0] = int(status[0] == 0)
status[1] = int(status[1] == 0)
push_cnt = 1
# 두번째 전구부터 만들고자 하는 상태와 현재 상태 비교
for i in range(1, N):
    # i-1번 전구의 상태가 다르면 i+1번 스위치 켜기
    if status[i-1] != target[i-1]:
        push_cnt += 1

        # 전구 상태 변경
        # current[i+1] = 1 if current[i+1]==0 else 0
        status[i] = int(status[i] == 0)
        if i < N-1:
            status[i+1] = int(status[i+1] == 0)
# N번째 전구 상태 확인
if status[N-1] == target[N-1]:
    result = min(result, push_cnt)

print(-1 if result == 1e9 else result)
