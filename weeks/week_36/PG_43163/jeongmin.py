visited = [False] * 50
step = 1e9

def dfs(begin, target, words, n, l, cnt):
    global step
    
    # target과 같아졌다면
    if begin==target:
        # 최소 몇 단계의 과정을 거쳤는지 저장
        step= min(step, cnt)
    
    # words 단어 확인
    for i in range(n):
        # 이미 변환된 적이 있는 단어라면
        if visited[i]:
            continue
        
        # 차이나는 알파벳 개수 구하기
        diff = 0
        for j in range(l):
            if begin[j]!= words[i][j]:
                diff += 1
        
        # 한 개의 알파벳만 차이나야함
        if diff == 1:        
            visited[i] = True
            dfs(words[i], target, words, n, l, cnt+1)
            visited[i] = False
    

def solution(begin, target, words):
    answer = 0
    
    n = len(words)
    l = len(words[0])
    
    # words 배열에 target이 있는 경우에 변환 가능
    if target in words:
        dfs(begin, target, words, n, l, 0)
    
        answer = step
    
    return answer