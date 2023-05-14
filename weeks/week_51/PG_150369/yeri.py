def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n-1
    p_idx = n-1
    while d_idx > -1 or p_idx > -1 :
        deliver = 0
        pick = 0
        res = 0
        # deliver
        for i in range(d_idx,-1,-1):
            if deliver + deliveries[i] <=cap:
                deliver += deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= (cap-deliver)
                res = max(res, d_idx)
                d_idx = i
                break
            if i == 0:
                if deliver == 0:
                    res=-1
                else:
                    res = max(res, d_idx)
                d_idx = -1
        # pick
        for i in range(p_idx,-1,-1):
            if pick + pickups[i] <=cap:
                pick += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= (cap-pick)
                res = max(res, p_idx)
                p_idx = i
                break
            if i == 0:
                if pick == 0:
                    res=-1
                else:
                    res = max(res, p_idx)
                p_idx = -1
        answer += (res+1)*2
    return answer
