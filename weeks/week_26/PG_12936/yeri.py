def makeFac(n):
    temp=[1]
    for i in range(2,n):
        temp.append(temp[-1]*i)
    return temp[::-1]
def solution(n, k):
    if n==1 : return [1]
    answer = []
    fac = makeFac(n)
    num=[ i for i in range(1,n+1)]
    for f in fac:
        pos, k = divmod(k,f)
        if k==0: pos-=1
        answer.append(num[pos])
        num.pop(pos)
    return answer+num
    