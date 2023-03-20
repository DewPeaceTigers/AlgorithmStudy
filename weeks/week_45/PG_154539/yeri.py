def solution(numbers):
    answer = [-1]*len(numbers)
    stack = [(numbers[0],0)]
    for i in range(1,len(numbers)):
        while stack and stack[-1][0] < numbers[i]:
            b,idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append((numbers[i],i))
    return answer