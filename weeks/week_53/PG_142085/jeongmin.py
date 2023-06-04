"""
# 힙큐 사용하기
q(힙큐): 무적권을 사용한 라운드 병사의 수
    - len(q) < k 이면 무적권 사용했다고 가정
    - len(q) == k 이면 
        무적권 사용 후보 중 최소값 < enemy[i] 일때 힙큐에서 최솟값 꺼낸 후 그 수만큼 남은 병사의 수 감소

remain: 남은 병사의 수
    - remain <=0 이면 게임 종료!
"""

import heapq


def solution(n, k, enemy):
    answer = 0

    # 남은 병사의 수
    remain = n

    q = []

    for e in enemy:
        # 무적권이 남은 경우
        if len(q) < k:
            heapq.heappush(q, e)

        else:
            # 무적권을 사용한 라운드의 병사 수 중 최솟값이랑 enemy[i] 값 비교
            if q[0] < e:
                x = heapq.heappop(q)
                heapq.heappush(q, e)
            else:
                x = e

            # 남은 병사 수 업데이트
            remain -= x

        # 남은 병사가 없다면 게임 종료!
        if remain < 0:
            break

        # 막은 라운드 수 증가
        answer += 1

    return answer
