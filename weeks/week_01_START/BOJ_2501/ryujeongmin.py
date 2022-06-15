''' [풀이]
1. divisor 리스트에 약수 저장
  - (default : 1 저장)
  - 약수 구하기 : 2부터 n//2 까지 반복하면서 체크 
  - (마지막에 n 저장)
2. divisor 리스트 길이 & k 비교
  - len(divisor) < k : 0 출력
  - len(divisor) ≥ k : k번째 약수 → divisor[k-1]
'''

# 두 개의 자연수 N, K 입력
# 1<=N<=10000 , 1<=K<=N
n, k = map(int, input().split())

# 약수 저장 리스트 (default: 1 저장)
divisor = [1]

# 약수 구하기
for i in range(2, n//2+1):
  if n%i==0:
    divisor.append(i)

# 자기 자신(n) 추가
divisor.append(n)

# N의 약수의 개수가 K개 보다 적어서 K번째 약수가 존재하지 않을 경우
if len(divisor)<k:
  # 0 출력
  print(0)
# N의 약수들 중 K번째로 작은 수를 출력
else:
  print(divisor[k-1])