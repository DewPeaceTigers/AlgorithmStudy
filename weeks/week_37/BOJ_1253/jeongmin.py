from itertools import combinations
import sys

input = sys.stdin.readline

# 수의 개수 N(1 ≤ N ≤ 2,000)
N = int(input())

# i번째 수를 나타내는 Ai(|Ai| ≤ 1,000,000,000, Ai는 정수)
A = list(map(int, input().split()))

# A 정렬
A.sort()

# 좋은 수의 개수는 몇 개인지 저장
cnt = 0

for i in range(N):
    # i번째 원소를 제외한 리스트 생성
    tmp = A[:i] + A[i+1:]

    left, right = 0, len(tmp)-1
    while left < right:
        x = tmp[left] + tmp[right]
        if x == A[i]:
            cnt += 1
            break
        # x를 증가시켜야 하므로 left 증가
        if x < A[i]:
            left += 1
        # x를 감소시켜야 하므로 right 감소
        else:
            right -= 1
            
print(cnt)