def solution(weights):
    answer = 0

    # 시소 짝꿍이 가능한 비율
    # 1/2, 2/3, 3/4, 1, 4/3, 3/2, 2
    ratio = [1/2, 2/3, 3/4, 1, 4/3, 3/2, 2]

    w = [0] * 2001
    for weight in weights:
        # 시소 짝꿍이 가능한 사람 찾기
        for r in ratio:
            # 정수일 경우
            idx = int(r*weight)
            if idx == r*weight and w[idx]:
                # 해당 몸무게의 사람 수만큼 시소 짝꿍 쌍의 수 증가시키기
                answer += w[idx]

        # 현재 무게에 해당하는 경우 1 증가
        w[weight] += 1

    return answer
