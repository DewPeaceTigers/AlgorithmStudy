'''[풀이]
1. 이중 반복문 사용하여 N 이하의 자연수 중 소수 구하기
2. M 이상 N 이하의 자연수 소수인지 확인하여
    sum 변수에 더하기, 최솟값 비교
'''

# M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값 구하기

# 자연수 M, N 입력 ( 1<= M <= N <= 10000 )
M = int(input())
N = int(input())

# 소수 구하기
isPrime = [1]*(N+1)

# 0, 1 소수 아님
isPrime[0], isPrime[1] = 0, 0

# N이하의 자연수 중 소수 구하기
for i in range(2, int(N**(1/2))+1):
  for j in range(i, N+1, i):
    if isPrime[j] and j!=i:
      isPrime[j]=0

# M 이상 N이하의 자연수 중 소수들의 합, 최솟값
sum, min =0, 10000

for i in range(M, N+1):
  if isPrime[i]:
    sum+=i
    if min > i:
      min = i

# 소수가 없을 경우 -1 출력
if sum==0:
  print(-1)
else:
  print(sum)
  print(min)