def solution(record):
    messages = []
    answer=[]
    users = {}
    for r in record:
        message=''
        if r[0]=='E':
            command, uid, name = r.split(' ')
            message='님이 들어왔습니다.'
            users[uid] = name
        elif r[0]=='L':
            command, uid = r.split(' ')
            message = '님이 나갔습니다.'
        elif r[0]=='C':
            command, uid, name = r.split(' ')
            message = 'c'
            users[uid] = name
        messages.append([uid,message])
    for message in messages:
        if message[1]=='c': continue
        answer.append(users[message[0]]+message[1])
    return answer