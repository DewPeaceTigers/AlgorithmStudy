"""
[ 풀이 찾아봄 ]
https://school.programmers.co.kr/questions/25471
https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

- 2차원으로 확장한 누적합을 이용하는 문제
"""


def solution(board, skill):
    answer = 0

    # 행, 열의 길이
    N, M = len(board), len(board[0])

    # 누적합 계산을 위한 배열
    calc_arr = [[0]*(M+1) for _ in range(N+1)]

    for t, r1, c1, r2, c2, degree in skill:
        """
        (r1, c1) ~ (r2, c2) 까지에 degree만큼의 변화를 주고 싶다면

            (r1, c1)   =  degree, (r1, c2+1)   = -degree,
            (r2+1, c1) = -degree, (r2+1, c2+1) =  degree

        만큼의 값을 더해주면 원하는 부분에 원하는 변화량만큼 값을 바꿀 수 있음
        """
        # 내구도 낮추기
        if t == 1:
            degree *= -1

        calc_arr[r1][c1] += degree
        calc_arr[r1][c2+1] -= degree
        calc_arr[r2+1][c1] -= degree
        calc_arr[r2+1][c2+1] += degree

    # 계산한 배열을 오른쪽으로 누적합
    for r in range(N):
        for c in range(1, M):
            calc_arr[r][c] = calc_arr[r][c-1] + calc_arr[r][c]

    # 계산한 배열을 아래쪽으로 누적합
    for c in range(M):
        for r in range(1, N):
            calc_arr[r][c] = calc_arr[r-1][c] + calc_arr[r][c]

    # 기존 배열에 누적합 더하기
    for r in range(N):
        for c in range(M):
            board[r][c] += calc_arr[r][c]

            # 계산한 값이 1 이상이면 파괴되지 않은 건물
            if board[r][c] >= 1:
                answer += 1

    return answer
