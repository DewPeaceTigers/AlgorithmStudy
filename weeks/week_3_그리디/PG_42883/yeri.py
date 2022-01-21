# 효율성 통과하지 못했다.
# from collections import deque
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     boats=deque()
#     cnt=0
#     for p in range(len(people)-1,-1,-1): # sort reverse 안쓰려고 뒤에서부터 index함
#         isFit=0
#         while isFit < len(boats): # 배 몇개 검사했는지 확인
#             if people[p] <= boats[0]: # 보트 남은 무게보다 작을 경우 태울 수 있음
#                 cnt+=1
#                 isFit="done"
#                 boats.popleft()
#                 break
#             else: # 태울 수 없음
#                 isFit+=1
#                 boats.rotate(-1) # 맨 앞을 맨 뒤로 보냄
#         if isFit!="done" : # done이 아니라면 들어갈 곳이 없었으니 보트 하나 만들어주기
#             if limit-people[p]+people[0]>limit: # 그 값이 너무 커서 가장 작은 값이 들어가도 limit을 넘친다면
#                 cnt+=1
#             else: boats.append(limit-people[p]) # 태우고 남은 무게
#     return len(boats)+cnt

## 다른 사람 풀이
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0 # 가장 작은 인덱스
    right = len(people) - 1 # 가장 큰 인덱스
    while left < right: # 오름차순을 지키고 있는 상태라면 
        if people[left] + people[right] <= limit: # 가장 작은 것과 가장 큰것의 합이 limit보다 작으면 태울 수 있음
            left += 1 # 다음 작은 것
            right -= 1 # 다음 큰 것
        else: # limit을 넘친다면
            right -= 1 # 다음 큰 것 (배 하나에 태운 셈)
        answer += 1 # 배 하나에 태움
    if left == right: # 둘이 같다면
        answer += 1 # 아직 하나가 안탄 거니깐 태우기

    return answer