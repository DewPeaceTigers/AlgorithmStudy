## 런타임 에러
## 사실 수학 문제였다.
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int,input().split())

    # 직전 K 이동시 k-1, k, k+1
    def move(before, cur, movement):
        global min_move
        if cur >= y: return
        if min_move <= movement: return
        if cur == y-1:
            min_move = min(min_move,movement+1)
            return
        for b in range(before-1,before+2):
            if b == 0: continue
            if cur+b == y-1:
                if b not in [0,1,2]: continue
            move(b,cur+b,movement+1)
    min_move = int(1e9)
    move(1,x+1,1)
    print(min_move)