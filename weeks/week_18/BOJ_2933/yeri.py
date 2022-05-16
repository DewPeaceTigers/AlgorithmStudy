import sys
input = sys.stdin.readline

R,C = map(int,input().split())
boards = [list(map(int,input().split())) for _ in range(R)]
throws = list(map(int,input().split()))

def drop():

def throw(n,s,e,add):
    # 왼쪽에서 던짐. 2로 나눠떨어지는 순서에
    for j in range(s,e,add):
        if boards[n][j]=='X':
            boards[n][j]='.'
            return j

for t in range(len(throws)):
    # length = 6 . 1=> 5 , 2=>4, 3=>3 4=>2, 5=>1, 6=>0
    # length-throw
    if t%2==0:
        where = R-throws[t]
        j = throw(where,0,C,+1)
    else:
        where = R-throws[t]
        j = throw(where,C-1,-1,-1)