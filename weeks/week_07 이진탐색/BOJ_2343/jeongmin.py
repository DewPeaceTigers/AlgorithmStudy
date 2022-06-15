import sys
input= sys.stdin.readline

# 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N) 입력
N, M = map(int, input().split())

# 각 강의의 길이(10,000분 이하) 입력
L = list(map(int, input().split()))

# 가능한 블루레이 크기중 최소 저장
size = 0

# 가능한 블루레이의 크기 범위 : L의 최댓값 ~ L[M-1:]의 합
start, end = max(L), sum(L[M-1:]) 

# 이분탐색 수행
while start<=end:
  mid = (start+end)//2
  # print(mid)
    
  # 기타 강의들의 길이 합, 블루레이의 수 저장
  sum, m = 0, 0
  for l in L :
    if sum+l<= mid: 
      sum += l
    else:
      m+=1 # 블루레이의 수 증가
      sum=l

  if m<M : # 가능한 블루레이 수 m이 M보다 작으면
    size = mid
    end = mid-1 # 블루레이의 크기 줄이기
  else:
    start = mid+1 # 블루레이의 크기 늘리기

  # print(start, end)

print(size)