'''
dp[i][j] : i행 j열을 밟았을 때 최대 점수
'''
def solution(land):
    n=len(land)
    
    for i in range(1, n) :
        for j in range(4) :
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])

            
    return max(land[n-1])