''' [풀이]
상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수
-> 결국에는 신장 트리를 만드는 형태
-> 트리의 간선 개수 : 노드 개수 -1
-> 따라서 답은 N-1 이다.
'''

import sys
input = sys.stdin.readline

# 테스트 케이스의 수 T(T ≤ 100) 입력
T = int(input())

for _ in range(T):
  # 국가의 수 N(2 ≤ N ≤ 1 000), 비행기의 종류 M(1 ≤ M ≤ 10 000) 입력
  N, M = map(int, input().split())
  for _ in range(M):
    a, b = map(int, input().split())

  print(N-1)