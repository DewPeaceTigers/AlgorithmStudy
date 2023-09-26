# 코너도 고려해야 하는 줄 알았는데 고려할 필요가 없었음..
# https://school.programmers.co.kr/questions/53910

def solution(m, n, startX, startY, balls):
    answer = []

    # 공을 적어도 벽에 한 번은 맞춘 후 목표 공에 맞힌다
    for a, b in balls:
        up, down, left, right = 1e9, 1e9, 1e9, 1e9

        # 위
        up = (startX-a)**2 + (2*n-startY-b)**2

        # 아래
        down = (startX-a)**2 + (startY+b)**2

        # 왼
        left = (startY-b)**2 + (startX+a)**2

        # 오른
        right = (startY-b)**2 + (2*m-startX-a)**2

        # x좌표 값이 같다면
        if startX == a:
            # startY가 b보다 클 때 아래쪽 벽면 불가능(벽면에 맞기 전에 공에 맞음)
            if startY > b:
                down = 1e9
            # startY가 b보다 작을 때 위쪽 벽면 불가능
            else:
                up = 1e9

        # y좌표 값이 같다면 왼쪽, 오른쪽 벽면에는 부딪힐 수 없음
        if startY == b:
            # startX가 a보다 클 때 왼쪽 벽면 불가능(벽면에 맞기 전에 공에 맞음)
            if startX > a:
                left = 1e9
            # startX가 a보다 작을 때 오른쪽 벽면 불가능(벽면에 맞기 전에 공에 맞음)
            else:
                right = 1e9

        dist = min(up, down, left, right)
        answer.append(dist)

    return answer
