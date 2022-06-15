''' [풀이]
1. n이 0이거나 1일 경우 n 출력
2. n이 2 이상인 경우
    - 반복문 이용해서 피보나치 수 구하기
'''

# n 입력 (n은 20보다 작거나 같은 자연수 또는 0)
n = int(input())

# 피보나치 수 구하기
if n==0 or n==1:
  print(n)
else:
  a, b, c = 0, 1, 1
  for i in range(2, n+1):
    c = a + b
    a, b = b, c

  print(c)