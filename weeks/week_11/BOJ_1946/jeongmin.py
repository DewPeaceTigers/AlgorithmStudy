import sys
input = sys.stdin.readline

# 케이스의 개수 T(1 ≤ T ≤ 20) 입력
T = int(input())

for _ in range(T):
  ans = 1
  # 지원자의 숫자 N(1 ≤ N ≤ 100,000) 입력
  N = int(input())
  
  # 각각의 지원자의 서류심사 성적, 면접 성적의 순위
  rank = [list(map(int, input().split())) for _ in range(N)]

  # 정렬(서류심사 성적 순위 높은 순)
  rank.sort(key= lambda x:x[0])

  pre = rank[0]
  for r in rank[1:]:
    # 면접 성적의 순위가 이전 지원자보다 더 높아야 함
    if pre[1]>r[1]:
      ans+=1
      pre = r
    
  print(ans)