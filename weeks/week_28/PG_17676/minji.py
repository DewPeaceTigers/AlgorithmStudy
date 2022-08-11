def check(logs, start, end) :
    count=0
    for log in logs :
        if log[0]<end and log[1]>=start:
            count+=1
            
    return count

def solution(lines):
    answer = 0
    logs=[]
    
    for line in lines :
        infos=line.split()
        h, m, s=infos[1].split(':')
        end=(int(h)*3600+int(m)*60+float(s))*1000
        start=end-float(infos[2][:-1])*1000+1
        logs.append([start, end])
    
    print(logs)
    for log in logs:
        answer=max(answer, check(logs, log[0], log[0]+1000), check(logs, log[1], log[1]+1000))
    return answer
