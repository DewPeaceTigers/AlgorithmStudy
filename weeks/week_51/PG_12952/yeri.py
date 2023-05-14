def solution(n):
    global grid, answer, queen
    answer = 0
    queen = [-1]*n
    def check(depth,i):
        for x in range(depth):
            if queen[x] == i or abs(queen[x]-i) == depth - x : return False
        return True
    def dfs(depth):
        global answer
        if depth == n :
            answer+=1
            return
        for i in range(n):
            if not check(depth,i):
                continue
            queen[depth]=i
            dfs(depth+1)
    for i in range(n):
        queen[0]=i
        dfs(1)
    return answer