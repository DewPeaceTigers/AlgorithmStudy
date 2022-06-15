'''[풀이]
1. 1000까지의 소수 구하기 (이중 반복문 사용)
2. N개의 각 숫자가 소수인지 확인
'''

# 수의 개수 N 입력 (N<=100)
N = int(input())
nums = list(map(int, input().split()))

# 소수인지 저장 (1000까지)
isPrime = [1]*1001

# 0, 1 초기화
isPrime[0], isPrime[1] =0, 0

# 1000까지의 소수 구하기
for i in range(2, int(1000**(1/2))+1):
  if isPrime[i]:
    for j in range(i, 1001, i):
      if isPrime[j]==1 and j!=i:
        isPrime[j]=0

# 소수의 개수 저장
cnt=0

# N개의 수 - 소수인지 확인
for n in nums:
  if isPrime[n]:
    cnt+=1

print(cnt)