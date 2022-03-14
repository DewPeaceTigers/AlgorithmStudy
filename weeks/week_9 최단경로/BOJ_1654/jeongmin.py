''' [풀이]
N개를 만들 수 있는 랜선의 최대 길이
-> 매개변수 탐색 : 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제

조건: sum(각 랜선의 길이 // L) >= N
    L: N개 랜선 하나의 길이
N개의 랜선 각각의 길이(L)를 이분탐색함
 - 가능한 범위 : 0 <= L =< 2^31-1
'''

import sys
input= sys.stdin.readline

# K, N 입력 (1 ≤ K ≤ 10,000, 1 ≤ N ≤ 1,000,000)
K, N = map(int, input().split())

# 랜선의 길이 입력
cable = [int(input()) for _ in range(K)]

start, end = 0, 2**31-1
L=0 # N개 랜선 하나의 길이 저장

# 매개변수 탐색 수행
while(start<=end):
  mid = (start+end)//2

  count=0
  # 랜선 개수 구하기
  count = sum([c//mid for c in cable])  

  # 조건을 만족하는 경우 (H 늘리기)
  if count>=N:
    start = mid+1
    L = mid # H 길이 mid로 갱신

  # 조건을 만족하지 않는 경우(H 줄이기)
  else:
    end = mid-1

print(L)