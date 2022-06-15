''' [풀이]
1. pos (위치) 변수 활용
2. n이 0이 아닐 때 반복
  - n%2 ==1 확인
  - n을 2로 나눈 값 n에 저장
  - pos 값 1 증가
'''

# 테스트 케이스 개수 T 입력
T = int(input())

# (1 ≤ T ≤ 10, 1 ≤ n ≤ 10**6)

for t in range(T):
  # n 입력
  n = int(input())

  # 위치
  pos = 0
  
  while n!=0:
    # 1의 위치 출력
    if n%2==1:
      print(pos, end=' ')
    n//=2 
    pos+=1