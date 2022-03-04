def solution(triangle):
    answer = 0
    
    # 거쳐간 숫자의 합 저장
    sum = [[0]*(i+1) for i in range(len(triangle))]

    sum[0][0] = triangle[0][0]
    
    for i in range(len(triangle)-1):
        for j in range(i+1):
            # 왼쪽 이동
            sum[i+1][j]= max(sum[i+1][j], sum[i][j]+triangle[i+1][j])
            
            # 오른쪽 이동
            sum[i+1][j+1]= max(sum[i+1][j+1], sum[i][j]+triangle[i+1][j+1])

    answer = max(sum[len(triangle)-1])
    
    return answer