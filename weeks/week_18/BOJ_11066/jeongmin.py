""" 풀이 찾아봄..."""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    files = [*map(int, input().split())]
    minCost = [[0] * K for _ in range(K)]  # 메모이제이션 리스트

    # 연속합 (a부터 b까지의 부분연속합을 구할 때, b까지합 - (a-1)까지합 으로 구해주면 됨)
    # 여러번 sum함수 안써도 되고, 딕셔너리 구해두면 O(1) 연산으로 그때그때 부분합 구해서 쓰는게 효율적
    subSum = {-1: 0}
    for idx in range(K):
        subSum[idx] = subSum[idx - 1] + files[idx]

    for size in range(1, K):  # size 크기로 묶은 그룹들의 minCost 구하기
        for start in range(K - 1):  # 그룹의 시작 인덱스 범위는 0부터 K-2까지
            end = start + size

            # 특정 size로 그룹핑했는데 end가 벗어난다면 size 그룹핑 그만두고 다음으로 넘어가기
            if end >= len(files):
                break

            result = float("inf")
            # 어떤 구간의 최소비용 minCost는, cut을 기준으로 분할할 때, 좌측 그룹의 최소 비용 + 우측 그룹의 최소 비용 + 좌측 압축 수와 우측 압축 수 더하기
            # 이 때 좌측 압축 수 + 우측 압축 수는 그 구간의 모든 수의 합과 같음
            for cut in range(start, end):
                result = min(result, minCost[start][cut] + minCost[cut + 1][end] + subSum[end] - subSum[start - 1])

            minCost[start][end] = result

    print(minCost[0][-1])