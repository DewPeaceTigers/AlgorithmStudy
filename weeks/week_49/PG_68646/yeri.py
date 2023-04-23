def find(start,end,increase,arr):
    m_l = int(1e9)
    res = 0
    for i in range(start,end,increase):
        if arr[i] < m_l:
            m_l = arr[i]
            res+=1
    return res
def solution(a):
    answer = 0
    min_n = min(a)
    min_i = a.index(min_n)
    
    return find(0,min_i,1,a)+find(len(a)-1,min_i-1,-1,a)