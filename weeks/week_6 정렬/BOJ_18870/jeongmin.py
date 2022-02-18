import sys
input = sys.stdin.readline

# N 입력
N = int(input())

coord = list(map(int, input().split()))

# 중복 제거, 정렬
# 딕셔너리에 값, 인덱스로 저장
coord_dict = {}
for i, c in enumerate(sorted(set(coord))):
  coord_dict[c] = i

for c in coord:
  print(coord_dict[c], end=' ')