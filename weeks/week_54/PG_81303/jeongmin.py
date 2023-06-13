"""
풀이 찾아봄!
- 링크드리스트 (dict 자료구조 사용)
"""


def solution(n, k, cmd):
    cur = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)
