import heapq


def solution(n, works):
    answer = 0

    # 최댓값이 작아지도록 해야함! 최대힙 사용하기
    q = []

    for w in works:
        heapq.heappush(q, -w)

    for i in range(n):
        x = heapq.heappop(q)

        # 모든 작업 수행 완료
        if x == 0:
            break

        # 1시간 동안 일 수행
        heapq.heappush(q, x+1)

    # 야근지수 구하기
    for x in q:
        answer += x**2

    return answer
