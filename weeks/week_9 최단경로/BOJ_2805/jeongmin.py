''' [풀이]
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
-> 매개변수 탐색 : 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제

조건: 절단기로 잘린 나무의 길이 합 >= M
절단기의 높이(H)를 이분탐색함
 - 가능한 범위 : 0 <= H =< max(tree)-1
'''

import sys
input= sys.stdin.readline

# 나무의 수 N, 나무의 길이 M 입력 (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
N, M = map(int, input().split())

# 나무의 높이 입력
tree = list(map(int, input().split()))

start, end = 0, max(tree)-1
H=0 # 절단기의 높이 저장

# 매개변수 탐색 수행
while(start<=end):
  mid = (start+end)//2

  sum=0
  # 절단기로 잘린 나무의 길이 합 구하기
  for t in tree:
    if t>mid:
      sum+=t-mid

  # 조건을 만족하는 경우 (H 늘리기)
  if sum>=M:
    start = mid+1
    H = mid # H 길이 mid로 갱신

  # 조건을 만족하지 않는 경우(H 줄이기)
  else:
    end = mid-1

print(H)