from collections import deque
def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [0 for _ in range(len(words))]
    ans = 999
    if target not in words:
        return 0

    while queue:
        word, depth = queue.popleft()
        if word == target:
            ans = min(ans, depth)
            break

        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for b, w in zip(word, words[i]):
                    if b != w:
                        cnt += 1
                if cnt == 1:
                    queue.append([words[i], depth + 1])
                    visited[i] = 1
    return ans