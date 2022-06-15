import sys
input = sys.stdin.readline

# 단어의 개수 N 입력
N = int(input())

word = [input().rstrip() for _ in range(N)]
word= list(set(word)) # 단어 중복 제거
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
word.sort(key=lambda x: [len(x), x])

print(*word, sep='\n')