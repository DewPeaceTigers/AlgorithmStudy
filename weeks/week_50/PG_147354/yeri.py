def solution(data, col, row_begin, row_end):
    result = []
    data.sort(key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin, row_end+1):
        result.append(sum([ n%i for n in data[i-1]]))
    answer = 0
    for r in result:
        answer ^= r
    return answer