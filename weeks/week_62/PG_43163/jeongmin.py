answer = 0

check = []

# cur : 현재 단어
# level : 몇 단계 거쳤는지
# L : 단어 길이
# N : words 단어 개수


def dfs(cur, level, l, n, target, words):
    global answer, check

    # 현재 단어랑 target이 같다면
    if cur == target:
        answer = level
        return

    for i in range(n):
        if check[i]:
            continue

        # 차이나는 알파벳 개수
        cnt = 0
        for x in range(l):
            if cur[x] != words[i][x]:
                continue
            cnt += 1

        # 한 개의 알파벳만 다른 경우
        if cnt == l-1:
            check[i] = True
            dfs(words[i], level+1, l, n, target, words)
            check[i] = False


def solution(begin, target, words):
    global answer, check

    l = len(begin)
    n = len(words)

    # 단어를 사용했는지 체크
    check = [False]*(n)

    dfs(begin, 0, l, n, target, words)

    print(answer)

    return answer
