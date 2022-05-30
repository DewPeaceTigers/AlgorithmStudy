"""
최대, 최소값 설정 잘하기..

교점 판별식 중에서 A * B * D - A * B * C 라고 하면
A B D가 각 100,000인 최댓값이고, 
C가 0이라면 결국 가장 큰 값인 (10^5)^3 = 10^15 = 1,000,000,000,000,000가 된다.
"""

from itertools import combinations

def solution(line):
    answer = []
    
    # 좌측 상단, 우측 하단 좌표
    minX, minY, maxX, maxY = 1e15, 1e15, -1e15, -1e15
    
    # 교점 저장
    point = set()
    # 교점 확인
    for l1, l2 in combinations(line, 2):
        a, b, e = l1
        c, d, f = l2
        
        # 하나의 교점이 발생하는 경우
        if a*d !=b*c:
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            
            # 정수로만 표현되는 좌표
            if x==int(x) and y==int(y):
                x, y = int(x), -int(y)
                point.add((x, y))
                if minX > x:
                    minX = x
                if minY > y:
                    minY = y
                if maxX <x:
                    maxX = x
                if maxY < y:
                    maxY = y
    
    h = maxY - minY + 1 # 세로 길이
    w = maxX - minX + 1 # 가로 길이

    # 격자판 만들기
    board = [["."]*w for i in range(h)]
    for x, y in point:
        # 별 채우기
        board[y-minY][x-minX] ="*"

    for b in board:
        answer.append("".join(b))
    return answer