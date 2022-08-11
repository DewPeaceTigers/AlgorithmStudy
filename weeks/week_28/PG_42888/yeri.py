def solution(records):
    nicks = {}
    msgs = []
    for record in records:
        if record.count(' ')==2: order, uid, nick = record.split(' ')
        else: 
            order, uid = record.split(' ')
            nick = ''
        if order[0] == 'E':
            nicks[uid] = nick
            msgs.append([uid,"님이 들어왔습니다."])
        elif order[0] == 'L':
            msgs.append([uid,"님이 나갔습니다."])
        elif order[0] == 'C':
            nicks[uid] = nick
    answer=[]
    for uid, msg in msgs:
        answer.append(nicks[uid]+msg)
    return answer