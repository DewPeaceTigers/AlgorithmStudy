def solution(rows, columns, queries):
    answer = []

    arr = [[(i-1)*columns+j for j in range(columns+1)] for i in range(rows+1)]

    for x1, y1, x2, y2 in queries:
        # 좌측상단에 있는 원소
        tmp = arr[x1][y1]

        # 가장 작은 숫자 저장
        num = arr[x1][y1]

        # 시계방향 이동
        # 위쪽 방향
        for i in range(x1+1, x2+1):
            arr[i-1][y1] = arr[i][y1]
            num = min(num, arr[i-1][y1])
        # 왼쪽 방향
        if arr[x2][y1+1:y2+1]:
            num = min(num, min(arr[x2][y1+1:y2+1]))
            arr[x2][y1:y2] = arr[x2][y1+1:y2+1]
        # 아래쪽 방향
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i-1][y2]
            num = min(num, arr[i][y2])
        # 오른쪽 방향
        if arr[x1][y1+1:y2]:
            num = min(num, min(arr[x1][y1+1:y2]))
            arr[x1][y1+2:y2+1] = arr[x1][y1+1:y2]

        arr[x1][y1+1] = tmp

        answer.append(num)

    return answer
