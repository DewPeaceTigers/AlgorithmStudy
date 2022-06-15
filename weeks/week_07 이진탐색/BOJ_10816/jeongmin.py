import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

# 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000) 입력
N = int(input())

# 숫자 카드에 적혀있는 정수 입력
cards = list(map(int, input().split()))

# 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M(1 ≤ M ≤ 500,000)개의 정수 입력
M = int(input())

m_cards=list(map(int, input().split()))

# 숫자 카드 정렬
cards.sort()

# 정답 저장
ans =[0]*M

for i, m in enumerate(m_cards):
  right_idx = bisect_right(cards, m)
  left_idx = bisect_left(cards, m)
  ans[i]=right_idx-left_idx

print(*ans)