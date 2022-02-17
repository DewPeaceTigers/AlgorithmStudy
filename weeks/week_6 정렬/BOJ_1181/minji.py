'''
import sys

n=int(input())
words=[]
for i in range(n) :
    word=sys.stdin.readline().strip()
    word_len=len(word)
    words.append((word, word_len))
words=list(set(words)) #중복제거
words.sort(key=lambda x:(x[1], x[0])) #길이순으로 정렬, 동일한 길이는 사전순서

for word in words :
    print(word[0])
'''
#이게 조금더 빠름
import sys

n=int(input())
words=[]
for i in range(n) :
    words.append(sys.stdin.readline().strip())
words=list(set(words)) #중복 제거
words.sort() #사전 순 정렬
words.sort(key=len) #길이 순 정렬

for word in words :
    print(word)