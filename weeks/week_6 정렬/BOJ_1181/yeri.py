import sys
input = sys.stdin.readline
n=int(input())
words=[]
for _ in range(n):
    tmp = input().strip()
    words.append(tmp)
words=list(set(words)) # 중복 거르기
words.sort(key=lambda x:(len(x),x)) # 길이 기준, 사전 기준 정렬 하기
for word in words:
    print(word)