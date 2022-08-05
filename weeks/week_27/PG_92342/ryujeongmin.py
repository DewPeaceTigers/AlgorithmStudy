"""
조건 잘 확인하기!!
"라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요."
"""


import copy # 깊은 복사 이용

answer = [-1] # 무조건 지거나 비기는 경우는 -1 리턴
diff = 1    # 라이언과 어피치 점수 차

# 우선순위 비교
def compare(arr1, arr2):
    if len(arr2)==1:
        return True
    
    # 가장 낮은 점수를 더 많이 맞힌 경우
    for i in range(10, -1, -1):
        if arr1[i]>arr2[i]:
            return True
        elif arr1[i]<arr2[i]:
            return False
    

# 라이언 점수, 라이언의 남은 화살 수
def shoot(apeach, lion, cnt, arrow, idx, info):
    global diff, answer
    score = 10-idx

    # 과녁판을 벗어나면 종료
    if idx>10:
        if(lion - apeach >= diff):
            # 점수차가 같은 경우 우선순위 비교
            if (lion-apeach == diff) and not compare(arrow, answer) :
                return
            
            diff = lion - apeach    # 점수차
            # print("[어피치] 점수: ", apeach, " [라이언] 점수: ", lion, " [점수차이]: ", diff)
            
            # 만약 화살이 남았다면 마지막에 넣어줌
            arrow[-1] = cnt  
            answer = arrow
        return

    # 라이언이 k점 획득하는 경우
    if info[idx]<cnt:
        arrow[idx] = info[idx]+1

        shoot(apeach, lion+score, cnt-arrow[idx], arrow.copy(), idx+1, info)

    # 라이언이 k점을 획득하지 않는 경우
    arrow[idx] = 0
    if info[idx] ==0: score = 0    # a=b=0 : 아무도 점수 못 가져감
    shoot(apeach+score, lion, cnt, arrow.copy(), idx+1, info) 
        

def solution(n, info):
    
    # 라이언 화살 개수 저장
    arrow = [0]*11
    
    shoot(0, 0, n, arrow, 0, info)
    
    return answer