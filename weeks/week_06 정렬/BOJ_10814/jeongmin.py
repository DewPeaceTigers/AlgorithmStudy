import sys
input = sys.stdin.readline

# 온라인 저지 회원의 수 N 입력
N = int(input())

profile = [input().split() for _ in range(N)]

# 나이순 정렬
profile.sort(key=lambda x: int(x[0]))

for p in profile:
  print(*p)