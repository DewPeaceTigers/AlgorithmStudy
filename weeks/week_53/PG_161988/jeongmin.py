# 누적합 이용..

def solution(sequence):
    answer = 0

    N = len(sequence)

    # 펄스 수열 : 두 가지 경우
    # [1, -1, 1, -1, ...]
    # [-1, 1, -1, 1, ...]
    sum1, sum2 = 0, 0  # 누적합, 누적합의 최솟값
    min1, min2 = 0, 0
    for i in range(N):
        if i % 2 == 0:
            sum1 += sequence[i]
            sum2 -= sequence[i]
        else:
            sum1 -= sequence[i]
            sum2 += sequence[i]

        # 누적합의 최솟값 저장
        min1 = min(min1, sum1)
        min2 = min(min2, sum2)

        # 펄스 수열의 합 중 가장 큰 것 구하기
        answer = max(sum2-min2, sum1-min1, answer)

    return answer
