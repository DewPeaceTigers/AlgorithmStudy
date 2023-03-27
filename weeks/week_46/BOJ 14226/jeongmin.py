from collections import deque
import sys

input = sys.stdin.readline 

S = int(input())

q = deque()
# 현재 이모티콘 개수, 클립보드에 있는 개수
q.append((1, 0))

# 방문 표시를 딕셔너리로 표현
visited = dict()
visited[(1, 0)] = 0

# BFS 수행
while q:
    now, clip = q.popleft()

    # 현재 이모티콘 개수가 s개라면
    if now == S:
        # 걸린 시간 출력
        print(visited[(now, clip)])
        break

    # 1. 화면에 있는 이모티콘 모두 복사해 클립보드에 저장
    if (now, now) not in visited:
        visited[(now, now)] = visited[(now, clip)] + 1
        q.append((now, now))

    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if (now+clip, now) not in visited:
        visited[(now+clip, clip)] = visited[(now, clip)] +1
        q.append((now+clip, clip))

    # 3. 화면에 있는 이모티콘 중 하나를 삭제하기
    if (now-1, clip) not in visited:
        visited[(now-1, clip)] = visited[(now, clip)] + 1
        q.append((now-1, clip))        
