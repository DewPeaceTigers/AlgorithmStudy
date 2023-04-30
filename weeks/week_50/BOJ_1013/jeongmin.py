# 풀이 찾아봄!
# match() : 문자열 처음부터 시작해서 패턴에 일치하는지 확인하는 형태
# fullmatch() : 문자열 전체가 해당 패턴인지를 검사함

import re
t = int(input())
for i in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")

### =========================== 틀린 코드

# # 정규표현식 : (100+1+|01)+

# import sys
# import re

# input = sys.stdin.readline 

# # 정규표현식 패턴
# p = re.compile('(100+1+|01)+')

# T = int(input())
# for _ in range(T):
#     target = input().rstrip()

#     m = p.match(target)

#     # 패턴이랑 일치하는 문자열이 없다면 None을 반환함
#     while m:
#         # 패턴이 일치하는 부분 문자열 제거
#         s, e = m.start(), m.end()

#         target = target[:s] + target[e:]

#         m = p.match(target)
    
#     # 제시한 패턴이랑 일치하다면 target 문자열은 빈 문자열로 남게 됨
#     if target:
#         print("NO")
#     else:
#         print("YES")


"""
re.compile() : 탐욕적으로 (최대한 많이) 매칭을 진행함

>>> 반례
Input
1
100111001

Answer
YES
(10011 / 1001)

Output
NO
(100111 / 001)
"""