def solution(s) :
    answer=len(s)
    if len(s) == 1:
        return 1
    
    for i in range(1, (len(s)//2)+1) :
        temp=s[:i]
        count=1
        new_s=''
        
        for j in range(i, len(s), i) :
            if temp==s[j:j+i] :
                count+=1
            else :
                if count==1 :
                    new_s+=temp
                else:
                    new_s+=str(count)+temp
                
                temp=s[j:j+i]
                count=1
        if count==1 :
            new_s+=temp
        else:
            new_s+=str(count)+temp
           
        if answer >= len(new_s) :
            answer=len(new_s)

    return answer

