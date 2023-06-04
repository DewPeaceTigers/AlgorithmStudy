def isValid(x,y,kind, answer):
    if kind==0:
        # 기둥
        if y==0 or [x,y,1] in answer or [x,y-1,0] in answer or [x-1,y,1] in answer:
            return True
    else:
        if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
            return True
    return False
def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        if b==0:
            # 삭제
            answer.remove([x,y,a])
            for tx,ty,ta in answer:
                if not isValid(tx,ty,ta,answer):
                    answer.append([x,y,a])
                    break
        else:
            # 설치
            if isValid(x,y,a,answer):
                answer.append([x,y,a])
        answer.sort()
    return answer