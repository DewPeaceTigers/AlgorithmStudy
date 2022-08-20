import sys

input=sys.stdin.readline

num1=str(input().rstrip("\n"))
num2=str(input().rstrip("\n"))

roma_num={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roma_num2={'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

def to_num(num) :
    answer=0
    visit=[False]*len(num)
    
    for i in range(len(num)) :
        if not visit[i] :
            if i+1<len(num) and num[i:i+2] in roma_num2 :
                answer+=roma_num2[num[i:i+2]]
                visit[i:i+2]=True, True
            else:
                answer+=roma_num[num[i]]
                visit[i]=True
        #print(answer)
    return answer

def to_str(n) :
    s=""
    while n>0:
        if n>=1000:
            s+="M"
            n-=1000
        elif n>=900:
            s+="CM"
            n-=900
        elif n>=500:
            s+="D"
            n-=500
        elif n>=400:
            s+="CD"
            n-=400
        elif n>=100:
            s+="C"
            n-=100
        elif n>=90:
            s+="XC"
            n-=90
        elif n>=50:
            s+="L"
            n-=50
        elif n>=40:
            s+="XL"
            n-=40
        elif n>=10:
            s+="X"
            n-=10
        elif n>=9:
            s+="IX"
            n-=9
        elif n>=5:
            s+="V"
            n-=5
        elif n>=4:
            s+="IV"
            n-=4
        elif n>=1:
            s+="I"
            n-=1
    return s

ans=to_num(num1)+to_num(num2)
print(ans)
print(to_str(ans))