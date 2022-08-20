def solution(N, number):
    ans = -1
    dp =[]
    for i in range(1,9):
        print(dp)
        nums =set()
        nums.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for a in dp[j]:
                print(i,j,a)
                for b in dp[-j-1]:
                    nums.add(a+b)
                    nums.add(a-b)
                    nums.add(a*b)
                    if(b!=0):
                        nums.add(a//b)
        if number in nums:
            ans = i
            break
        dp.append(nums) 
    return ans
