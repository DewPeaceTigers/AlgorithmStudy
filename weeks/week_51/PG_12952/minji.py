def dfs(queen, row, n) :
    cnt=0
    
    if n==row :
        return 1
    for col in range(n) :
        queen[row]=col
        
        for i in range(row) :
            if queen[row]==queen[i] : #세로
                break
            
            if abs(queen[i]-queen[row])==abs(i-row) : #대각선
                break
        else:
            cnt+=dfs(queen, row+1, n)
            
    return cnt
        
    
def solution(n):
    answer = 0
    
    queen=[0]*n
    return dfs(queen, 0, n)
