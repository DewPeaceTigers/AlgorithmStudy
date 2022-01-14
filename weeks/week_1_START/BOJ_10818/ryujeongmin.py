''' [풀이]
최댓값, 최소값 구하기
    - 파이썬 내장함수 (min 함수, max 함수) 이용
'''

# 정수의 개수 N (1 ≤ N ≤ 1,000,000) 입력
N = int(input())

# 정수 입력
nums = list(map(int, input().split()))

# 최소값, 최대값 출력
print(min(nums), max(nums))