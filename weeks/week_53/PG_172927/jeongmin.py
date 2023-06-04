"""
# 그리디 알고리즘 사용
    - 5개씩 나눠서 diamond, iron, stone 개수 저장
    - diamond, iron, stone 개수가 많은 순으로 리스트 정렬
    - picks 곡괭이를 차례로 사용하면서 피로도 계산
 => 이 방법은 테스트 8이 실패함..
 
5개씩 자르는 부분이 잘못됨!! 곡괭이 수만큼 5개씩 자르고 정렬을 해야함다
"""

from collections import deque


def solution(picks, minerals):
    answer = 0

    minerals_cnt = []

    # 곡괭이 개수
    picks_cnt = sum(picks)

    # 광물 수
    N = len(minerals)

    # 곡괭이로 캘 광물 그룹 수 (광물을 곡괭이 수 만큼 앞에서부터 잘라야 함)
    n = min(N//5, picks_cnt)

    # 5개씩 나누어서 diamond, iron, stone 순으로 개수 저장
    for i in range(n):
        cnt = {'diamond': 0, 'iron': 0, 'stone': 0}

        for j in range(5):
            cnt[minerals[5*i+j]] += 1

        minerals_cnt.append([cnt['diamond'], cnt['iron'], cnt['stone']])

    # 곡괭이 개수가 더 많아 모든 광물을 캘 수 있는 경우
    if picks_cnt > n:
        # 5개로 나누었을 때 나머지 부분
        cnt = {'diamond': 0, 'iron': 0, 'stone': 0}
        for i in range(N-5*n):
            cnt[minerals[5*n+i]] += 1
        minerals_cnt.append([cnt['diamond'], cnt['iron'], cnt['stone']])

    # diamond, iron, stone 개수가 많은 순으로 정렬
    minerals_cnt.sort(key=lambda x: [-x[0], -x[1], -x[2]])

    # 곡괭이를 차례로 사용하여 광물 캐기
    q = deque(minerals_cnt)

    # 다이아몬드 곡괭이 사용
    for x in range(picks[0]):
        # 모든 광물을 캔 경우 종료!
        if not q:
            break

        mineral = q.popleft()

        answer += sum(mineral)

    # 철 곡괭이 사용
    for x in range(picks[1]):
        # 모든 광물을 캔 경우 종료!
        if not q:
            break

        mineral = q.popleft()

        answer += (mineral[0]*5 + mineral[1] + mineral[2])

    # 돌 곡괭이 사용
    for x in range(picks[2]):
        # 모든 광물을 캔 경우 종료!
        if not q:
            break

        mineral = q.popleft()
        answer += (mineral[0]*25 + mineral[1]*5 + mineral[2])

    return answer
