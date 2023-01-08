def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left+right)//2
        if mid == 0: break

        zero_gap=0
        for i in range(len(stones)):
            if stones[i]-mid <=0 : zero_gap+=1
            else: zero_gap=0

            if zero_gap == k : break
        if zero_gap == k : right = mid -1
        else:
            left = mid+1

    return left