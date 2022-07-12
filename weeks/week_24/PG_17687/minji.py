def solution(n, t, m, p):
    answer = ''
    num="0123456789ABCDEF"
    convert_list=[]
    def convert(i, n) : #n진수로 변환
        q, r=divmod(i, n)
        if q==0 :
            return num[r]
        else:
            return convert(q, n)+num[r]
        
    for i in range(t*m) : #list에 저장
        conv=convert(i, n)
        for c in conv :
            convert_list.append(c)
    
    for i in range(p-1, t*m, m) : 
        answer+=convert_list[i]
    return answer