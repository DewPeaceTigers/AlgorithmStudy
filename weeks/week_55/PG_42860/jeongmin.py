"""
[풀이 찾아봄]
https://velog.io/@doeunllee/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-42860%EB%B2%88-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
조이스틱이 움직이는 횟수 = (커서를 이동하는 횟수) + (알파벳을 "A"에서 원하는 알파벳까지 이동하는 횟수)

- 알파벳 이동횟수는 고정되어 있음
- 커서를 이동하는 횟수의 최소값을 구해야 함!!
    min( 2i + n - ind, i + 2n - ind ) = min( i, n - ind ) + (i + n - ind)
    (i를 현재 위치, n은 전체 길이, ind는 연속된 전체 A 다음의 값 위치)
"""


def solution(name):
    answer = 0

    # 알파벳을 만들기 위한 최소 조작 횟수
    alphabet = {chr(ord('A')+i): (26-i if i > 13 else i) for i in range(26)}

    # name의 길이
    N = len(name)

    min_length = N-1

    cnt = 0
    for i in range(N):
        # 알파벳 이동횟수
        cnt += alphabet[name[i]]

        # 커서 이동
        next = i + 1
        # 연속된 A 구하기
        while next < N and name[next] == 'A':
            next += 1

        min_length = min(min_length, i+N-next + min(i, N-next))

    answer += min_length    # 커서 이동 횟수
    answer += cnt           # 알파벳 이동 횟수

    return answer
