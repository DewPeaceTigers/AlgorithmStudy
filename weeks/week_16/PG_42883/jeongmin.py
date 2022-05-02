# number에서 k개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자

def solution(number, k):
    answer = ''
    
    # 스택 사용
    stack = []
    # 앞에서 부터 차례로 확인
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        
    # k가 0보다 큰 경우 뒤에 숫자 제외
    if k != 0:
        stack = stack[:-k]
        
    answer = "".join(stack)
            
    return answer