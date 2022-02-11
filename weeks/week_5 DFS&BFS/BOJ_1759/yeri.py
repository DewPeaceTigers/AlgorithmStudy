"""
1. 암호 dfs로 만들기
2. 자음, 모음 개수 확인하기
"""
import sys
import re
m = re.compile('[aeiou]')
input = sys.stdin.readline
L,C=map(int,input().split())
letters=list(map(str,input().split()))
letters.sort()

def dfs(cnt=0,pw=[],start=0):
    if cnt==L:
        temp=''.join(pw)
        len_m= len(m.findall(temp)) # 정규식을 통해 모음 개수 세기 
        if len_m>=1 and len(pw)-len_m>=2: # 자음 개수는 전체 예비번호 길이에서 모음 개수 빼서 구할 수 있다.
            print(temp)
        return
    else:
        for i in range(start,C):
            if letters[i] not in pw:
                pw.append(letters[i])
                dfs(cnt+1,pw,i+1)
                pw.pop()
dfs()