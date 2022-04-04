import sys
input = sys.stdin.readline

# 수열의 길이 N (50이하 자연수) 입력
N = int(input())

nums = []  # 양수 저장
nums_n = []  # 0이나 음수 저장
# 수열 원소 입력
for _ in range(N):
    n = int(input())
    if n <= 0:
        nums_n.append(n)
    else:
        nums.append(n)

# 절댓값 큰 순으로 정렬
nums.sort(reverse=True)
nums_n.sort()

sum = 0  # 수 묶기 수행 후 합 (양수)
sum_n = 0  # 수 묶기 수행 후 합 (0, 음수)

pre = 0
for i, n in enumerate(nums_n):
    if i % 2 == 0:
        pre = n
    else:  # 짝수 번
        sum_n += pre * n
        pre = 0
sum_n += pre

pre = 0
for i, n in enumerate(nums):
    if i % 2 == 0:
        pre = n
    else:
        if pre == 1 or n == 1:
            sum += pre + n
        else:
            sum += pre * n
        pre = 0
sum += pre
print(sum + sum_n)
"""
4
-1
1
2
3

6
"""