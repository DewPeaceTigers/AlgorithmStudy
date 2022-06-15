''' [풀이]
거스름돈 문제!
'Ai는 Ai-1의 배수' 라는 문제 조건이 있으므로 그리디 알고리즘을 사용
  - 가치가 높은 동전부터 차례로 구한다.
'''
import sys
input = sys.stdin.readline

# N: 동전 종류 수, K: 가치의 합 
# N과 K 입력 (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
N, K = map(int,input().split())

# 동전의 가치 A 입력(오름차순)
A = [int(input()) for _ in range(N)]
A.reverse() # 내림차순으로 변경

# 동전의 개수
cnt=0
price = K

for coin in A:
  cnt+= price // coin
  price %= coin

print(cnt)