'''
X_index[i][0]:입력 받은 값
X_index[i][1]:입력 받았을 때 index
X_index[i][2]:출력값
'''
n=int(input())
X=list(map(int, input().split()))
X_index=[[0]*3 for i in range(n)]
for i in range(n) :
    X_index[i][0]=X[i]
    X_index[i][1]=i
X_index.sort(key=lambda x:x[0]) #입력 받은 값 크기 순으로 정렬

for i in range(1, n) :
    if X_index[i-1][0] == X_index[i][0] : #앞의 값과 같으면 같은 값
        X_index[i][2]=X_index[i-1][2]
    else:
        X_index[i][2]=X_index[i-1][2]+1 #앞의 값과 다르면 + 1
X_index.sort(key=lambda x:x[1])#처음 입력받았을때 인덱스기준으로 정렬

for i in range(n) :
    print(X_index[i][2], end=' ')