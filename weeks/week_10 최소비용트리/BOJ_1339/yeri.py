"""
못품..
자릿수를 세서 그 크기 역순서대로 숫자 9부터 할당
"""

import sys
input=sys.stdin.readline

n=int(input())
words=[input().strip() for _ in range(n)]

alphabets={}
num=9

for word in words:
    len_word=len(word)
    for i in range(len_word):
        if word[i] not in alphabets:
            alphabets[word[i]]=10**(len_word-i)
        else: alphabets[word[i]]+=10**(len_word-i)
exp=''

hashResult = list(dict(sorted(alphabets.items(), reverse=True, key= lambda x: x[1])).keys())
num=9
for hr in hashResult:
    alphabets[hr]=str(num)
    num-=1

form=''
for word in words:
    temp=''
    for w in word:
        temp+=alphabets[w]
    form+=str(int(temp))+'+'

print(eval(form[:-1]))