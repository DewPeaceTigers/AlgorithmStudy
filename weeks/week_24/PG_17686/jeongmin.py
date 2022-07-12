def solution(files):
    answer = []
    
    info = []   # 파일 정보 저장
    for f, file in enumerate(files):
        num = False
        
        # NUMBER, TAIL 시작 인덱스 저장
        idx1, idx2 = len(file), len(file)
        
        # 파일명 세 부분으로 구분하기
        # HEAD(대소문자 구분 없음), NUMBER, TAIL
        for i, c in enumerate(file):
            if c.isdecimal() and num == False:
                num = True
                idx1 = i
            if not c.isdecimal() and num == True:
                idx2 = i
                break
        info.append([file[:idx1].lower(), int(file[idx1:idx2]), f])
    
    info.sort(key=lambda x: [x[0], x[1], x[2]])
    
    for x in info:
        answer.append(files[x[2]])
              
    return answer