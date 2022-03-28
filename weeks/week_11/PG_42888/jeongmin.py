# 채팅방 메시지
# Enter 들어옴: "[닉네임]님이 들어왔습니다." 
# Leave 나감: "[닉네임]님이 나갔습니다."
# Change 닉네임을 변경하는 방법
#   1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어감
#   2. 채팅방에서 닉네임 변경

def solution(record):
    answer = []
    result = [] # 출력 내용
    
    user = {} # 사용자
    for r in record:
        chat = r.split()
        # print(chat)
        
        # 나가기
        if chat[0] == "Leave":
            # print("나가기")
            result.append(("Leave", chat[1]))
        
        else:
            uid, nickname = chat[1], chat[2]
            user[uid] = nickname
            
            # 들어가기
            if chat[0] =="Enter":
                # print("들어가기")
                result.append(("Enter", chat[1]))
                
            # 변경하기
            else:
                user[uid] = nickname
                
    # 채팅창 내용 출력
    for x in result:
        if x[0] == "Enter":
            answer.append(user[x[1]]+"님이 들어왔습니다.")
        else:
            answer.append(user[x[1]]+"님이 나갔습니다.")
    return answer