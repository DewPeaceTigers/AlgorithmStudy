# import sys
# import re
# input=sys.stdin.readline
# line = input()
# p= re.compile('(\d+)([-+])?') # 정규식으로 연산자, 피연산자 구분
# compiled = p.findall(line)
# query=''
# is_opened=False
# for com in compiled:
#     query+=str(int(com[0]))
#     if com[1]=='-': # 마이너스를 만나면 
#         if is_opened: # 괄호 여부를 찾아 괄호를 상황에 맞춰 정리
#             query+=')'+com[1]
#             is_opened=False
#         else:
#             query+=com[1]+'('
#             is_opened=True
#     else : query+=com[1] # 나머지는 그냥 더하기
# if is_opened : query+=')'
# print(eval(query))

## 틀린 이유
# 맨 처음 피연산자가 - 이면 맨 앞에 괄호를 두지 못함

## 답
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)