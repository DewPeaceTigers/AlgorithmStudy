def solution(arr):
    answer = [0, 0]
    n=len(arr)
    def compare(x, y, n) :
        tmp=arr[x][y]
        for i in range(x, x+n) :
            for j in range(y, y+n) :
                if arr[i][j] != tmp :
                    n2=n//2
                    compare(x, y, n2)
                    compare(x, y + n2, n2)
                    compare(x + n2, y, n2)
                    compare(x + n2, y + n2, n2)
                    return
        answer[tmp]+=1
    compare(0, 0, n)
    return answer