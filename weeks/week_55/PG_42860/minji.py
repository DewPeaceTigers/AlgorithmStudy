def solution(name):
    answer = 0
    n = len(name)
    init = 'A' * n

    min_move = n - 1  # 커서 좌우 최대 이동
    for idx in range(n):
        answer += min(ord('Z') - ord(name[idx]) + 1, ord(name[idx]) - ord('A'))
        next = idx + 1

        while next < n and name[next] == 'A':
            next += 1

        # 연속된 A의 왼쪽부터 시작, 연속된 A 오른쪽부터 시작
        min_move = min([min_move, 2 * idx + n - next, idx + 2 * (n - next)])

    return answer + min_move