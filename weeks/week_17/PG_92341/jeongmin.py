def solution(fees, records):
    answer = []
    
    car = dict() # 입차한 시간 저장
    time = dict() # 자동차 별 누적 시간 저장
    
    for record in records:
        t, num, info = record.split()
        
        # 입차
        if info=="IN":
            car[num] = t
        
        # 출차
        else:
            # 입차 시간
            in_time = car.pop(num)
            total = calc_time(t)- calc_time(in_time)
            
            # 시간 계산
            if num in time:
                time[num]+= total
            else:
                time[num] = total
    
    # 출차를 하지 않은 차가 있는 경우
    for num in car:
        total = calc_time("23:59")- calc_time(car[num])
        
        # 시간 계산
        if num in time:
            time[num]+= total
        else:
            time[num] = total
    
    # 누적 요금 계산
    for num, time in sorted(time.items()):
        # 기본 시간 이하
        if time <= fees[0]:
            answer.append(fees[1]) # 기본 요금
        # 기본 시간 초과
        else:
            # 초과한 시간
            add_time = time - fees[0]
            
            # 기본 요금 + 추가 요금
            answer.append(fees[1] + math.ceil(add_time/fees[2])* fees[3])
    
    return answer