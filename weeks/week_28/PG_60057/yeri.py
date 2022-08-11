def solution(data):
    if len(data)==1 : return 1
    short = int(1e9)
    for length in range(1,len(data)//2+1):
        temp = ''
        i = 0
        while i<len(data):
            cnt=1
            for j in range(i+length,len(data),length):
                if data[i:i+length] == data[j:j+length]: cnt+=1
                else: break
            if cnt!=1 :temp += str(cnt)+data[i:i+length]
            else : temp += data[i:i+length]
            i = i+length*cnt
        short = min(short,len(temp))
    return short