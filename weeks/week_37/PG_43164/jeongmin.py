from collections import defaultdict
import copy

results = []

def dfs(tickets, graph, start, cnt, result):
    if cnt == len(tickets):
        results.append(result)
        return
    
    if start in graph:
        for to in graph[start]:
            ngraph = copy.deepcopy(graph)
            ngraph[start].remove(to)
            dfs(tickets, ngraph, to, cnt+1, result+ " "+ to)
    

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    
    dfs(tickets, graph, "ICN", 0, "ICN")
    results.sort()

    answer = results[0].split()
    
    return answer