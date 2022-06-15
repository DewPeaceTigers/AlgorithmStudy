import sys
input= sys.stdin.readline

# 테스트 케이스의 개수 T 입력
T = int(input())

for _ in range(T):
  # 첫째 줄에는 A의 수 N과 B의 수 M 입력
  N, M = map(int, input().split())

  # A, B 크기 입력
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  # B 오름차순 정렬
  B.sort()

  # A가 B를 먹을 수 있는 쌍의 개수
  ans =0

  for i, a in enumerate(A):
    start, end = 0, M-1
    # print("========",a,"==========")
    while start<=end:
      mid = (start+end)//2
      
      if B[mid]<a: # 중간값이 a보다 작으면
        start=mid+1
      else:
        end = mid-1 # 중간값이 a보다 크거나 같으면
      
    ans += (end+1) # 개수이므로 인덱스+1
  print(ans)