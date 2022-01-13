''' [풀이]
collections 모듈 deque 사용
1. 제일 위에 있는 카드 버리기
    - queue.popleft() 
2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
    방법 1) queue.append(queue.popleft()) : 삭제하고 그 값 추가
    방법 2) queue.rotate(-1) : 음수면 왼쪽으로 회전
'''

from collections import deque

# N(1 ≤ N ≤ 500,000) 입력
N = int(input())

# N장의 카드 큐에 저장
queue = deque([ i for i in range(1, N+1)])

while(len(queue)>1):
  # 제일 위에 있는 카드 버림
  queue.popleft()
  # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
  queue.append(queue.popleft()) # queue.rotate(-1) 도 가능

# 마지막에 남은 카드
print(queue[0])