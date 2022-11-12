from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for w, l in results:
        win[l].add(w)  # 나를 이긴 사람
        lose[w].add(l)  # 나에게 진 사람

    for i in range(1, n + 1):
        for w in win[i]:
            lose[w].update(lose[i])
        for l in lose[i]:
            win[l].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer