'''
연산자 개수 - 후에 dfs호출하고 다시 +해주어야함.
'''
import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))
operation=list(map(int, input().split()))
minimum=1e9
maximum=-1e9

def dfs(depth, result, op):
    global minimum, maximum
    if depth == n :
        maximum=max(maximum, result)
        minimum=min(minimum, result)
        return
    if op[0] :
        op[0]-=1
        dfs(depth+1, result+num[depth], op)
        op[0]+=1
    if op[1]:
        op[1]-=1
        dfs(depth+1, result-num[depth], op)
        op[1]+=1
    if op[2]:
        op[2]-=1
        dfs(depth+1, result*num[depth], op)
        op[2]+=1
    if op[3]:
        op[3]-=1
        dfs(depth+1, int(result/num[depth]), op) # //로 계산하면 틀
        # (// 연산자는 답이 float로 나오는 것도 있지만 음수 나눗셈에서 -∞ 방향으로 버림을 하기 때문에 문제와 답 자체가 달라집니다. )
        op[3]+=1

dfs(1, num[0], operation)

print(maximum)
print(minimum)
