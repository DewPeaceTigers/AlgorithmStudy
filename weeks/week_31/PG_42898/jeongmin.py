def solution(m, n, puddles):
    answer = 0
    
    arr = [[-1]*m for i in range(n)]
    
    for x, y in puddles:
        arr[y-1][x-1] = 0
    
    # 테두리
    tmp = 1
    for y in range(n):
        if arr[y][0] == 0:
            tmp = 0
        
        arr[y][0] = tmp
        
    tmp = 1
    for x in range(m):
        if arr[0][x] == 0:
            tmp = 0
            
        arr[0][x] = tmp
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 0:
                continue
            
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
    answer = (arr[n-1][m-1])%1000000007
        
    return answer