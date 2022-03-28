''' [풀이]
'''
from collections import deque
import sys
input = sys.stdin.readline

gear = [[] for i in range(5)]
for i in range(1, 5):
  # 12시 방향부터 시계 방향 순으로 
  gear[i] = deque(list(input().rstrip()))

# 회전 횟수 K(1 ≤ K ≤ 100) 입력
K = int(input())

for _ in range(K):
  # 회전 여부 저장
  rot = [0]*5
  
  # 회전시킨 톱니바퀴의 번호, 방향 입력
  # 방향이 1인 경우 시계 방향, 0인 경우 반시계 방향
  num, dir = map(int, input().split())

  rot[num]= dir if dir else -1
  for i in range(num, 4):
    if gear[i][2] != gear[i+1][-2]:
      rot[i+1] = -rot[i] if rot[i] else 0
      # print("오른쪽 회전", rot)
  
  for i in range(num, 1, -1):
    if gear[i][-2] != gear[i-1][2]:
      rot[i-1] = -rot[i] if rot[i] else 0
      # print("왼쪽 회전", rot)
      
  for i in range(1, 5):
    gear[i].rotate(rot[i])
  
score = 0
for i in range(1, 5):
  if gear[i][0]=='1':
    score += 2**(i-1)
    
print(score)