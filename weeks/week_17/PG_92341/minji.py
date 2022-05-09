import math


def checkTime(first, second):
    h1, m1 = map(int, first.split(':'))
    h2, m2 = map(int, second.split(':'))
    return (h2 - h1) * 60 + (m2 - m1)


def solution(fees, records):
    answer = []
    car = {}
    check_time = {}
    for record in records:
        temp = record.split()
        if temp[2] == "IN":
            car[temp[1]] = temp[0]
        else:
            if temp[1] in check_time:
                check_time[temp[1]] += checkTime(car[temp[1]], temp[0])
            else:
                check_time[temp[1]] = checkTime(car[temp[1]], temp[0])
            car[temp[1]] = '0'
    for key, value in car.items():
        if value != '0':
            if key in check_time:
                check_time[key] += checkTime(value, "23:59")
            else:
                check_time[key] = checkTime(value, "23:59")

    check_time = sorted(check_time.items())

    for car, time in check_time:
        print(time)
        if time < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])

    return answer