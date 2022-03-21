'''
못품
A가 만의 자리와 십의 자리에 쓰였다면 10010이렇게 표현
word_list에 넣고 정렬하면 가장 크게 쓰인 부분부터 순서대로 정렬
그 순서로 9, 8, 7.., 1을 부여하면 됨
'''
import sys

N=int(input())
words=[]
word_dict={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
word_list=[]
for i in range(N):
    words.append(sys.stdin.readline())

for word in words :
    for i in range(len(word)-1) :
        num = 10 ** (len(word)-i-1)
        word_dict[word[i]] += num

for value in word_dict.values():
    if value > 0 :
        word_list.append(value)
answer=0
dict=sorted(word_list, reverse=True)
for i in range(len(dict)) :
    answer+=dict[i]*(9-i)

print(answer//10)