import math

def solution(progresses, speeds):
    answer = []
    
    # 기능 개수
    N = len(progresses)
    
    # 작업 일수 계산
    work = [0] * N
    for i in range(N):
        work[i] = math.ceil((100-progresses[i])/speeds[i])
    
    work_time, cnt = work[0], 1
    # 뒤의 작업 기간이 짧다면 배포 기능 +1
    for i in range(1, N):
        if work_time>=work[i]:
            cnt += 1
            continue
        
        # 작업 배포
        answer.append(cnt)
        
        work_time = work[i]
        cnt = 1
    
    answer.append(cnt)
        
    return answer