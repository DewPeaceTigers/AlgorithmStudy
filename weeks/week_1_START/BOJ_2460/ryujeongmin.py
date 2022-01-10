''' [풀이]
1. 정착역 별로 기차 안에 있는 사람 수 리스트(people_num)에 저장
    [i]번역에 타고 있는 사람 수 = [i-1]번역 타고 있던 사람 수 - [i]번역 내린 사람 수 + [i]번역 탄 사람 수
2. people_num 리스트의 최대값 출력
'''

# 내린 사람 수, 탄 사람 수
station_info=[]

# 정착역 별로 기차 안에 있는 사람 수
people_num=[0]*10

# 10개의 정착역 존재
for i in range(10):
  # 각 역에서 내린 사람 수 , 탄 사람 수 입력
  station_info.append(list(map(int, input().split())))

  if i==0:
    people_num[i] = station_info[i][1]
  else:
    # 타고 있던 사람 수 - 내린 사람 수 + 탄 사람 수
    people_num[i] = people_num[i-1]-station_info[i][0]+station_info[i][1]
  
print(max(people_num))