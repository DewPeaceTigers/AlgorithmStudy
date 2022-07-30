def getMaxMin(board, oper, i, j):
    ''' 
    입력
    board : bottom-up계산을 위한 리스트
    oper : 연산자가 담겨있는 리스트
    i, j : 인덱스
    출력
    -> i ~ j범위를 계산했을 때 최대, 최소 값을 반환한다.
    '''
    tmp = []
    for mid in range(i, j):
        if oper[mid] == '+':
            tmp.append(board[i][mid][0] + board[mid+1][j][0])
            tmp.append(board[i][mid][0] + board[mid+1][j][1])
            tmp.append(board[i][mid][1] + board[mid+1][j][0])
            tmp.append(board[i][mid][1] + board[mid+1][j][1])
        elif oper[mid] == '-':
            tmp.append(board[i][mid][0] - board[mid+1][j][0])
            tmp.append(board[i][mid][0] - board[mid+1][j][1])
            tmp.append(board[i][mid][1] - board[mid+1][j][0])
            tmp.append(board[i][mid][1] - board[mid+1][j][1])
        else:
            tmp.append(board[i][mid][0] * board[mid+1][j][0])
            tmp.append(board[i][mid][0] * board[mid+1][j][1])
            tmp.append(board[i][mid][1] * board[mid+1][j][0])
            tmp.append(board[i][mid][1] * board[mid+1][j][1])
    return max(tmp), min(tmp)

# 수식 길이
N = int(input())

# 피연산자의 길이
n = N // 2

# 수식 입력
formula = input()

# 피연산자, 연산자 
num, oper = [], []
for idx, item in enumerate(formula):
    if idx % 2 == 0:
        num.append(int(item))
    else:
        oper.append(item)

# bottom-up방식으로 풀기 위해 리스트 생성, 
# 가장 안쪽의 [0, 0]은 각 각 최솟값, 최댓값을 저장
board = [[[0, 0] for i in range(n+1)] for j in range(n+1) ]

# scope -> 최댓값과 최솟값을 구하려는 범위
# 적은 범위부터 최댓값, 최솟값을 구해 가며 각 경우들을 저장한다.
for scope in range(n+1):
    for i in range(0, n-scope+1):
        j = i + scope
        if i == j:
            board[i][j][0] = num[i]
            board[i][j][1] = num[i]
        else:
            maxV, minV = getMaxMin(board, oper, i, j)
            board[i][j][0] = maxV
            board[i][j][1] = minV

print(max(board[0][n]))