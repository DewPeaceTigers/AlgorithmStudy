def solution(sequence):
    arr1 = []
    arr2 = []
    idx = 1
    # 각 -1, 1 펄스의 곱들을 구해준다
    for i in range(len(sequence)):
        arr1.append(sequence[i] * idx)
        arr2.append(sequence[i] * (-idx))

        idx *= -1

    dp1 = [arr1[0]]
    dp2 = [arr2[0]]
    for i in range(1, len(sequence)):
        dp1.append(max(arr1[i], dp1[i - 1] + arr1[i]))
        dp2.append(max(arr2[i], dp2[i - 1] + arr2[i]))

    answer = max(max(dp1), max(dp2))

    return answer