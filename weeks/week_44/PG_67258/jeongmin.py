from collections import defaultdict

# 모든 보석을 하나 이상 포함하는 가장 짧은 구간 찾기
def solution(gems):
    answer = []
    
    # 보석 종류 저장
    kinds = set(gems)

    N = len(gems)
    K = len(kinds)
    
    # 적어도 1개 이상 포함하는지 저장
    check = {kind:False for kind in kinds}
    
    # 보석 수
    jewel = defaultdict(int)
    
    # 구간 길이
    section = 1e9
    
    # 왼쪽 포인터, 오른쪽 포인터
    l, r = 0, 0
    jewel[gems[l]] += 1
    
    while 0<=l<N and 0<=r<N:
        # print(l+1, r+1, jewel, section)
        
        # 모든 보석이 한번 이상 나왔다면
        if len(jewel)==K:
            # 구간 길이 
            if section > r-l:
                section = r-l
                answer = [l+1, r+1]
            
            # 맨 왼쪽 요소 제거
            jewel[gems[l]] -= 1
            if jewel[gems[l]] == 0:
                del jewel[gems[l]]
            
            # 왼쪽 포인터 이동
            l += 1
            
        # 보석이 덜 나왔다면
        else:
            r += 1
            
            # 보석 수 세기
            if r<N:
                jewel[gems[r]] += 1
            
    return answer

""" 시간 초과.. """
# # 모든 보석을 하나 이상 포함하는 가장 짧은 구간 찾기
# def solution(gems):
#     answer = []
    
#     # 보석 종류 저장
#     kinds = set(gems)

#     N = len(kinds)
    
#     # 적어도 1개 이상 포함하는지 저장
#     check = {kind:False for kind in kinds}
    
#     # 보석 저장 위치
#     pos = {kind:-1 for kind in kinds}
    
#     # 쇼핑한 보석 종류 수
#     cnt = 0
    
#     # 구간 길이
#     section = 1e9
    
#     minPos, maxPos = len(gems), 0
#     for i, gem in enumerate(gems):
#         # 쇼핑한 보석 체크
#         if not check[gem]:
#             check[gem] = True
#             cnt += 1
        
#         # 보석 위치 업데이트
#         pos[gem] = i
            
#         # 모든 보석을 적어도 1번 이상 산 경우
#         if cnt == len(kinds):
#             """ [효율성 테스트] 11~15 시간 초과.."""
#             # minPos, maxPos = min(pos.values()), max(pos.values())
            
#             """ [효율성 테스트] 12, 13, 15 시간 초과.."""
#             minPos, maxPos = min(pos.values()), i
#             # print(minPos, maxPos, i)
            
#             # 구간이 더 짧은 경우 업데이트
#             if section > maxPos-minPos:
#                 section = maxPos-minPos
#                 answer = [minPos+1, maxPos+1]
#                 # print(answer, pos)
    
#     return answer