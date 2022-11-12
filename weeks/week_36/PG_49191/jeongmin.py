# n명의 선수가 있을 때 한 선수의 승패정보를 n-1개 가지게 된다면, 해당 선수의 순위를 알 수 있음

def solution(n, results):
    answer = 0
    
    arr=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for a, b in results:
        arr[a][b]=1
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][j]==0 and (arr[i][k]==1 and arr[k][j]==1):
                    arr[i][j]=1

    # 선수별 가지고 있는 승패정보 개수 저장 
    result=[0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j]==1:
                result[i]+=1
                result[j]+=1
    
    for i in range(1, n+1):
        # 승패정보를 n-1개 가지고 있다면 순위 알 수 있음
        if result[i]==n-1:
            answer+=1
    
    return answer