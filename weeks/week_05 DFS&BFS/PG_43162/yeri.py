def dfs(n,queue,computers):
    route=[]
    while queue:
        com = queue.pop()
        route.append(com)
        for i in range(n):
            if computers[com][i]==1 and i not in route:
                queue.append(i)
                computers[com][i]=-1
    return route
def solution(n,computers):
    routes=[]
    for i in range(n):
        checkIn=False # 네트워크에 포함 돼있으면 확인하지 않도록
        for route in routes:
            if i in route: checkIn=True
        if not checkIn:
            routes.append(dfs(n,[i],computers))
    return len(routes)