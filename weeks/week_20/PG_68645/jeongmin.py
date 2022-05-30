def solution(n):
    tri = [[0]*i for i in range(1, n+1)]
    
    # 아래, 오른쪽, 대각선 위로 이동
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    # 시작 위치, 숫자, 방향
    x, y, num, d = -1, 0, 1, 0
    
    # 달팽이 채우기
    for l in range(n, 0, -1):
        for i in range(l):
            x = x + dx[d]
            y = y + dy[d]
            
            tri[x][y] = num
            
            num += 1
        # 방향 전환
        d = (d+1)%3
        
    # 2차원 리스트를 1차원 리스트로
    answer = sum(tri, [])
    
    return answer