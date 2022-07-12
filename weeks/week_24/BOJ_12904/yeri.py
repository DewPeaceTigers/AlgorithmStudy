import sys
input = sys.stdin.readline

s_str = list(input().strip())
t_str = list(input().strip())
n_str=t_str[:]
for i in range(len(t_str)-1,len(s_str)-1,-1):
    if n_str[i]=='A':
        n_str.pop()
    else:
        n_str.pop()
        n_str.reverse()
if s_str == n_str: print(1)
else : print(0)