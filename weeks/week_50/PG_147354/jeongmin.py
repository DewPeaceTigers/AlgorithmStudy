def solution(data, col, row_begin, row_end):
    answer = 0
    
    C = len(data[0])
    
    # 튜플 정렬
    data.sort(key=lambda x: [x[col-1], -x[0]])
    # print(data)
    
    # S_i 구하기
    xor = -1
    for i in range(row_begin, row_end+1):
        # 각 칼럼을 i로 나눈 나머지 합
        S_i = 0
        for x in range(C):
            S_i += data[i-1][x] % i
    
        # bitwise XOR 연산
        if xor == -1:
            xor = S_i
        else:
            xor = xor ^ S_i
    
    answer = xor
    
    return answer