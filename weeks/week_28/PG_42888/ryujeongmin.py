def solution(record):
    answer = []

    message = []    # 채팅방 메시지 관리
    nickname = {}   # 유저 닉네임 관리

    for r in record:
        info = r.split()

        if info[0] != 'Leave':
            # info[1]: 유저아이디, info[2]: 닉네임
            nickname[info[1]] = info[2]

            if info[0] == 'Change':
                continue
                
        # Enter/Leave, uid 저장
        message.append(info[0:2])
    
    for msg in message:
        if msg[0] == 'Enter':
            last_str = "님이 들어왔습니다."
        else:
            last_str = "님이 나갔습니다."

        answer.append(nickname[msg[1]]+last_str)

    return answer