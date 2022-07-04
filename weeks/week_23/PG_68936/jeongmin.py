"""
재귀함수 사용!
"""
answer = [0, 0]

def quadtree(x, y, n, arr):
    if n==1:
        answer[arr[x][y]]+=1
        return
    
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                quadtree(x, y, n//2, arr)
                quadtree(x+n//2, y, n//2, arr)
                quadtree(x, y+n//2, n//2, arr)
                quadtree(x+n//2, y+n//2, n//2, arr)
                return
    answer[num]+=1      

def solution(arr):
    quadtree(0, 0, len(arr), arr)
    
    return answer