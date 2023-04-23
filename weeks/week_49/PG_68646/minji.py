def solution(a):
    answer = 0
    n = len(a)
    result = [False] * n  # 자기가 가장 작은 경우 저장
    left_min, right_min = float('inf'), float('inf')

    for i in range(n):
        if a[i] < left_min:
            left_min = a[i]
            result[i] = True
        if a[n - i - 1] < right_min:
            right_min = a[n - i - 1]
            result[n - i - 1] = True

    return sum(result)