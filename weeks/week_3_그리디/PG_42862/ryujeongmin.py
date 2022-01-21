''' [풀이]
1. 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 처리
  - lost, reserve 리스트에서 학생 제거
2. lost, reserve 리스트 오름차순 정렬
3. reserve 반복문 돌며 가능한 학생에게 체육복 빌려줌
  - 빌린 학생 lost 리스트에서 제거
4. 답 : n - len(lost)
'''

def solution(n, lost, reserve):
    answer = 0
    
    reserve_copy = reserve.copy()

    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
    for r in reserve_copy:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    
    # 학생들 번호 오름차순으로 정렬
    lost.sort() 
    reserve.sort()
    
    for r in reserve:       
        # 앞 번호 학생에게 빌려주기
        if r-1 in lost:
            lost.remove(r-1)
        # 뒷 번호 학생에게 빌려주기
        elif r+1 in lost:
            lost.remove(r+1)

    answer = n- len(lost)
    
    return answer