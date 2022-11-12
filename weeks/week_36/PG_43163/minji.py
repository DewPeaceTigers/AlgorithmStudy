from collections import deque


def check_change(word, change_word):
    diff = 0
    for i in range(len(word)):
        if word[i] != change_word[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    if target not in words:
        return 0

    while q:
        word, depth = q.popleft()
        for change in words:
            if check_change(word, change):
                if target == change:
                    return depth+1
                else:
                    q.append([change, depth + 1])
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))