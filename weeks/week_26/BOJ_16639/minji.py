def getMaxMin(board, oper, i, j):
    ''' 
    �Է�
    board : bottom-up����� ���� ����Ʈ
    oper : �����ڰ� ����ִ� ����Ʈ
    i, j : �ε���
    ���
    -> i ~ j������ ������� �� �ִ�, �ּ� ���� ��ȯ�Ѵ�.
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

# ���� ����
N = int(input())

# �ǿ������� ����
n = N // 2

# ���� �Է�
formula = input()

# �ǿ�����, ������ 
num, oper = [], []
for idx, item in enumerate(formula):
    if idx % 2 == 0:
        num.append(int(item))
    else:
        oper.append(item)

# bottom-up������� Ǯ�� ���� ����Ʈ ����, 
# ���� ������ [0, 0]�� �� �� �ּڰ�, �ִ��� ����
board = [[[0, 0] for i in range(n+1)] for j in range(n+1) ]

# scope -> �ִ񰪰� �ּڰ��� ���Ϸ��� ����
# ���� �������� �ִ�, �ּڰ��� ���� ���� �� ������ �����Ѵ�.
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