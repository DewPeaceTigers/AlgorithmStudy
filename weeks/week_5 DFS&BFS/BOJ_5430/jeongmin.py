'''[풀이]
투 포인터(s,e) 사용
반복문을 돌면서 함수 수행
  1. R(뒤집기): turn 변수 값 변경
  2. D(버리기)
    - turn이 0인 경우(순서대로): 시작포인터(s)값 1 증가
    - turn이 1인 경우(역순) : 끝 포인터(e)값 1 감소
    - 배열이 빈 경우에는 error
x[s:e] -> turn이 0이면 순서대로 출력, turn이 1이면 역순으로 출력
'''

import sys
input=sys.stdin.readline 

# 테스트 케이스 입력
T = int(input())

for _ in range(T):
  err = False # 에러인 경우 True

  # 수행할 함수 p 입력
  p = input().rstrip()

  # 배열에 들어있는 수의 개수 n 입력
  n = int(input())
  x = input().rstrip()[1:-1].split(',') # [,] 제거 & 숫자만 저장

  # 시작 끝 포인터, 배열 순서 변수
  s, e, turn = 0, n, 0 

  for func in p:
    # R : 배열에 있는 수의 순서를 뒤집는 함수
    if func=='R':
      # turn 값 변경
      turn = 0 if turn else 1
    # D : 첫번째 수를 버리는 함수
    elif func=='D':
      if s<e:
        # turn이 1이면 뒤에 있는 수 제거
        if turn:
          e-=1
        # turn이 0이면 앞에 있는 수 제거
        else:
          s+=1
      # 배열이 빈 경우 D를 사용하면 에러
      else:
        err = True
        break

  if err:
    print('error')
  else:
    # turn이 0이면 순서대로 출력, turn이 1이면 역순으로 출력
    nums = x[s:e][::-1] if turn else x[s:e]
    print("["+",".join(nums)+"]")