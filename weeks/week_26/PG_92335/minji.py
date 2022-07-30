def change(n, k) :
    word=""
    while n>0 :
        word=str(n%k)+word
        n=n//k
    return word

def solution(n, k):
    answer = 0
    word=change(n, k)
    
    word=word.split("0")
    for w in word :
        if len(w) == 0 or int(w)==1 :
            continue
        
        isPrime=True
        for i in range(2, int(int(w)**0.5)+1) :
            if int(w)%i == 0 :
                isPrime=False
                break
        if isPrime==True:
            answer+=1
    return answer