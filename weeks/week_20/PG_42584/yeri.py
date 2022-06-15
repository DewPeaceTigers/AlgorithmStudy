def solution(prices):
    res=[0]*len(prices)
    stack=[0] # 주식 가격이 처음으로 떨어지는 위치를 아직 찾지 못한 가격의 index 모음
    for i in range(1,len(prices)):
        if prices[i]< prices[stack[-1]]:
            # 가격이 떨어졌다면
            for j in stack[::-1]: # Stack 뒤쪽이 괜찮다면 앞의 것들도 괜찮을 것이다.
                if prices[i]<prices[j]:
                    res[j] = i-j # 여태 거쳐온 인덱스 수
                    stack.remove(j) # 해당 index 삭제
                else : break # 아직 떨어지지 않음
        stack.append(i) # 비교한 인덱스 넣기
    for i in range(0,len(stack)-1):
        res[stack[i]]=len(prices)-stack[i]-1
    return res