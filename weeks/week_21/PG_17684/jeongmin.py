def solution(msg):
    answer = []
    
    # 사전 초기화
    dict = {chr(ord('A')+i): i+1 for i in range(26)}

    # 시작 인덱스, 사전에 있는 문자열 최대 길이, 색인 번호
    s, l, num = 0, 1, 26
    while s<len(msg):
        for ll in range(l, 0, -1):
            # 글자가 사전에 있으면
            if msg[s:s+ll] in dict:
                # print("글자 사전에 있음", msg[s:s+ll], dict[msg[s:s+ll]])
                # 색인번호 출력
                answer.append(dict[msg[s:s+ll]])
                
                num += 1    # 색인번호 1 증가
                
                # 다음 글자를 포함한 글자 사전에 추가
                dict[msg[s:s+ll+1]] = num
                
                s += ll
                l = max(l, ll+1)
                break
                
    return answer