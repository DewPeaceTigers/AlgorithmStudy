answer = 0


def dfs(index, value, numbers, target):
    global answer
    if index == len(numbers): #끝에 있는 number까지 다 이용했으면
        if value == target: #target과 같으면
            answer += 1
        return
    dfs(index + 1, value + numbers[index], numbers, target) #다음 숫자를 +하는 경우 
    dfs(index + 1, value - numbers[index], numbers, target) # 다음 숫자를 -하는 경우


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)

    return answer
