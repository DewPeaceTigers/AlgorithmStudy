from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    log_=defaultdict(list)
    for record in records:
        time,num,type = record.split(' ')
        log_[num].append([type,time])
    d_time, d_fee, a_time, a_fee = fees
    acc_=defaultdict(int)
    for num,log in log_.items():
        time=0
        for i in range(0,len(log),2):
            if i+1<len(log):
                in_h, in_m = map(int,log[i][1].split(':'))
                out_h, out_m = map(int,log[i+1][1].split(':'))
                time += (out_h*60+out_m)-(in_h*60+in_m)
            else:
                in_h,in_m = map(int,log[i][1].split(':'))
                time += 23*60+59 - (in_h*60+in_m)
        answer.append([num,d_fee if time <= d_time else d_fee+math.ceil((time-d_time)/a_time)*a_fee])
    answer.sort(key=lambda x:x[0])
    return [ time for _,time in answer]