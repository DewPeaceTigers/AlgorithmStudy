def make(n, q):
    rev_base = ''
    switch={'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
    if n==0 : return '0'
    while n > 0:
        n, mod = divmod(n, q)
        if str(mod) in switch:
            rev_base+=switch[str(mod)]
        else : rev_base += str(mod)
    return rev_base[::-1] 

def solution(n, t, m, p):
    answer = ''
    nums=''
    num=0
    next_p = p-1
    while len(answer)<t:
        nums+= make(num,n)
        num+=1
        if next_p <= len(nums)-1:
            answer+= nums[next_p]
            next_p+=m
    return answer