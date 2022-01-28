import sys
input = sys.stdin.readline
n,m=map(int,input().split())
boards=[]
for _ in range(n):
    temp = list(input())
    tempBoard=[]
    for i in range(m):
        if temp[i]=="W": # 비트마스크하기 위해 input 값도 0과 1로 처리 (0:white, 1: black)
            tempBoard.append(0)
        else:
            tempBoard.append(1)
    boards.append(tempBoard)
reals=[ # 8*8 비트 마스킹하기 위해 white로 시작한 것과 black으로 시작한 것 두개 나눠서 선언해둠
    [ # white
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]
    ],
    [ # black
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1]
    ]
] # 비트 마스크 이용
res=[]
for i in range(n+1-8): # input 기준으로 모든 8열 set를 돌기 위함
    for j in range(m+1-8): # input 기준으로 모든 8행 set를 돌기 위함
        tempW,tempB=0,0 # 각 real 보드를 트래킹하면서 각각 저장
        for const_i in range(8):
            for const_j in range(8):
                if boards[i+const_i][j+const_j] ^ reals[0][const_i][const_j] == 1:  # ^ 연산자를 통해 다르다면 반대로 바꿔야하기에 1 증가
                    tempW += 1
                if boards[i+const_i][j+const_j] ^ reals[1][const_i][const_j] == 1:  # ~ 위와 동일 ~
                    tempB += 1
        res.append(min(tempW,tempB)) # 두개 중 작은 것 저장
print(min(res)) # 저장된 것 중 가장 작은 것이 답
