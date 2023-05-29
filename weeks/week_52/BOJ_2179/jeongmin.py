import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

eng_words = defaultdict(list)
for _ in range(N):
    w = input().rstrip()

    for i in range(len(w)):
        # 접두사를 key로 하여 딕셔너리 저장
        k = w[:i+1]
        eng_words[k].append(w)

# key(접두사)의 길이가 긴 순으로 정렬
sorted_words = sorted(eng_words.items(), key=lambda x: len(x[0]), reverse=True)

find = False
for key, words in sorted_words:
    # print(key, words)
    n = len(words)
    if n == 1:
        continue

    # 두 단어가 똑같지 않다면
    for i in range(n-1):
        if words[i] != words[i+1]:
            print(words[i])
            print(words[i+1])

            find = True
            break

    if find:
        break
