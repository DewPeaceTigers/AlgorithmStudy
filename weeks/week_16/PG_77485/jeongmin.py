def solution(rows, columns, queries):
    answer = []
    
    # matrix = [list(range(i*columns+1, (i+1)*columns+1)) for i in range(rows)]
    matrix = [[i*columns+j for j in range(1, columns+1)] for i in range(rows)]
    
    # 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    d= 0  
    
    for q in queries:
        x1, y1, x2, y2 = q
        h, w = x2-x1, y2-y1
        cnt = [w, h, w, h]
        # print(cnt)
        
        # 초기 숫자 저장
        pre = matrix[x1-1][y1-1]
        
        # 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자 저장
        m = pre
        
        # 시작 위치 (x1-1, y1-1)
        x, y = x1-1, y1-1
        
        # 시계 방향 (동, 남, 서, 북 순으로)
        for i in range(4):
            # 가로/세로 길이 만큼
            for j in range(cnt[i]):
                x = x+ dx[i]
                y = y+ dy[i]
                
                # 작은 값 저장
                m = min(m, matrix[x][y])
                
                # 회전 이동 (값 변경)
                pre, matrix[x][y] = matrix[x][y], pre
                
        answer.append(m)
            
    
    return answer