def sector_4(arr):
    target = len(arr) // 2
    starts = [[0, 0], [target, 0], [0, target], [target, target]]

    res = [0, 0]
    for x, y in starts:
        new_arr = []
        check = 0
        for i in range(target):
            check += sum(arr[x + i][y:y + target])
            new_arr.append(arr[x + i][y:y + target])
        if check == 0:
            res[0] += 1
            continue
        if check == target * target:
            res[1] += 1
            continue
        next_res = sector_4(new_arr)
        res[0] += next_res[0]
        res[1] += next_res[1]
    return res


def solution(arr):
    one_arr_sum = sum(sum(arr,[]))
    if one_arr_sum==0: return [1,0]
    if one_arr_sum==len(arr)*len(arr): return [0,1]
    return sector_4(arr)