def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k=c
        arr = array[i-1:j] # 자르고
        arr.sort() # 그 배열 정렬 하고 
        answer.append(arr[k-1]) # k번째 뽑기
    return answer