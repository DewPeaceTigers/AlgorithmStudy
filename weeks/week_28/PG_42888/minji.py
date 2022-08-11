def solution(records):
    answer = []
    chat=[]
    id={}
    for record in records :
        if record.split()[0]=="Enter" or record.split()[0]=="Change":
            id[record.split()[1]]=record.split()[2]
            
    for record in records:
        if record.split()[0]=="Enter" :
            answer.append("{}���� ���Խ��ϴ�.".format(id[record.split()[1]]))
        elif record.split()[0]=="Leave" :
            answer.append("{}���� �������ϴ�.".format(id[record.split()[1]]))
    return answer