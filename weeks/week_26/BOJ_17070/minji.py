'''
���η� �� �� �ִ� ����� �� -> (���ο��� ���η� ����, �밢������ ���η� ����) �� ����� ������ ��

���η� �� �� �ִ� ����� �� -> (���ο��� ���η� ����, �밢������ ���η� ����) �� ����� ������ ��

�밢������ �� �� �ִ� ����� �� ->

 (���ο��� �밢�� ����, ���ο��� �밢�� ����, �밢������ �밢�� ����) �� ����� ������ ��
'''
n=int(input())
boards=[]
for _ in range(n) :
    boards.append(list(map(int, input().split())))
    
move=[[[0 for _ in range(n)] for _ in range(n)] for i in range(3)]
move[0][0][1]=1

for i in range(2, n) :
    if boards[0][i]==0 :
        move[0][0][i]=move[0][0][i-1]
        
for i in range(1, n) :
    for j in range(2, n) :
        if boards[i][j]==0 and boards[i][j-1]==0 and boards[i-1][j]==0 :
            move[2][i][j]=move[0][i-1][j-1]+move[1][i-1][j-1]+move[2][i-1][j-1]
        if boards[i][j]==0 :
            move[0][i][j]=move[0][i][j-1]+move[2][i][j-1]
            move[1][i][j]=move[1][i-1][j]+move[2][i-1][j]
            
print(move[0][n-1][n-1]+move[1][n-1][n-1]+move[2][n-1][n-1])