def solution(stones, k):
    answer = 0
    left, right=1, max(stones)

    while left<=right:
        cnt=0
        mid = (left + right) // 2
        for stone in stones :
            if(stone-mid)<=0 : cnt+=1
            else: cnt=0
            if cnt>=k: break
        if cnt<k :
            left=mid+1
        else:
            answer=mid
            right=mid-1
    return answer