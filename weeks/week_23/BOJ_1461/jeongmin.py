import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 책의 위치
book = list(map(int, input().split()))
book.sort()

# 위치가 0보다 큰 책 (내림차순)
positive = [b for b in book[::-1] if b>0]
p = len(positive)

answer = 0
# 0 보다 큰 경우
for i in range(0, p, M):
    answer += positive[i]
# 0 이하인 경우
for i in range(0, len(book)-p, M):
    answer += (-book[i])

# 각 위치 왕복(*2) - 다시 되돌아올 필요 없으므로 가장 먼거리 빼기
print(answer*2-max(abs(book[0]), abs(book[-1])))