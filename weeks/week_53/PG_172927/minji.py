from collections import Counter


def solution(picks, minerals):
    answer = 0
    pick_cnt = sum(picks)
    cost_list = []
    for i in range(0, len(minerals), 5):
        c = Counter(minerals[i:i + 5])
        costs = [0, 0, 0]  # 다이아몬드, 철, 돌맹이 곡괭이 순

        for key, value in c.items():
            if key == "diamond":
                costs[0] += 1 * value
                costs[1] += 5 * value
                costs[2] += 25 * value
            elif key == "iron":
                costs[0] += 1 * value
                costs[1] += 1 * value
                costs[2] += 5 * value
            else:
                costs[0] += 1 * value
                costs[1] += 1 * value
                costs[2] += 1 * value
        cost_list.append(costs)
        if len(cost_list) == pick_cnt:  # 곡괭이 수보다 많은 경우 제외
            break

    cost_list.sort(key=lambda x: (-x[2], -x[1]))
    for cost in cost_list:
        if picks[0] > 0:
            answer += cost[0]
            picks[0] -= 1
            continue
        elif picks[1] > 0:
            answer += cost[1]
            picks[1] -= 1
        else:
            answer += cost[2]
            picks[2] -= 1
    return answer