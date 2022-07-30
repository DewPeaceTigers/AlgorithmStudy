def solution(n, k):
    answer = []
    
    l1 = [i for i in range(1, n+1)]
    
    # 팩토리얼 구하기
    fac = [1] * 20
    for i in range(2, 20):
        fac[i] = fac[i-1]*i;

    x = n
    k-=1
    for i in range(n):
        idx = k//fac[x-1]
        
        answer.append(l1[idx])

        l1.pop(idx)
        
        k = k%fac[x-1]
        x -= 1
        
    return answer