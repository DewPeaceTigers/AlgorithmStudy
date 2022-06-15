def solution(array, commands):
    answer = []
    for i ,j, k in commands:
        sort_arr = array[i-1:j]  # 배열 자르기
        sort_arr.sort() # 배열 정렬
        answer.append(sort_arr[k-1]) # k번째 있는 수 구하기
    return answer