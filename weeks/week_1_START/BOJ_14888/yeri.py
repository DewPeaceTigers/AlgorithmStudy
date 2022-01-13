N = int(input())
A=list(map(int,input().split()))
ops=list(map(int,input().split())) # +,-,x,/
def makeFunc(n,p,m,t,d,res):
    global results
    #print(n,p,m,t,d,res)
    if n == N-1:
        results=[max(results[0],res),min(results[1],res)]
        return
    else:
        if p!=ops[0]: makeFunc(n+1,p+1,m,t,d,res+A[n+1])
        if m!=ops[1]: makeFunc(n+1,p,m+1,t,d,res-A[n+1])
        if t!=ops[2]: makeFunc(n+1,p,m,t+1,d,res*A[n+1])
        if d!=ops[3]: makeFunc(n+1,p,m,t,d+1,int(res/A[n+1]))
results=[int(-1e9),int(1e9)] #max,min
makeFunc(0,0,0,0,0,A[0])
print(results[0])
print(results[1])