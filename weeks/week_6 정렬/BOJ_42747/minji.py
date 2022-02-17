def solution(citations):
    answer = 0
    n=len(citations)
    citations.sort()
    for i in range(n) :
        h_index=n-i #오름차순 정렬을 하면 citations[i]이상 인용된건 뒤로 다 있음
        if citations[i]>=h_index : #citations[i]가 h번 이상 인용되었는지 확인
            answer=h_index
            break
    return answer