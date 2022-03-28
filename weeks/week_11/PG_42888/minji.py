def solution(records):
    answer = []
    chat = []
    id = {}
    for record in records:
        if record.split()[0] == "Enter" or record.split()[0] == "Change": #id등록에 따른 닉네임 저장
            id[record.split()[1]] = record.split()[2]

    for record in records:
        if record.split()[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id[record.split()[1]]))
        elif record.split()[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(id[record.split()[1]]))
    return answer