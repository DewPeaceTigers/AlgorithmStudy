import sys
sys.setrecursionlimit(10001)
def solution(nodeinfo):
    answer = [[]]
    nodes = {}
    for i,(x,y) in enumerate(nodeinfo):
        nodes[i+1] = (x,y)
    nodes = list(nodes.items())
    nodes.sort(key= lambda x:(-x[1][1],x[1][0]))
    root = -1
    hi = nodes[0][0]
    graph = {}
    for i,(x,y) in nodes:
        graph[i] = {
            'value':x,
            'left':-1,
            'right':-1
        }
        if root==-1:
            root = graph[i]
        else:
            cur = root
            while True:
                if cur['value'] < x:
                    if cur['right']==-1:
                        cur['right'] = i
                        break
                    else:
                        cur = graph[cur['right']]
                else:
                    if cur['left'] == -1:
                        cur['left'] = i
                        break
                    else:
                        cur = graph[cur['left']]
    def pre(root, now):
        if root == -1: return now
        node = graph[root]
        now.append(root)
        pre(node['left'],now)
        pre(node['right'],now)
        return now
    def post(root,now):
        if root == -1: return now
        node = graph[root]
        post(node['left'],now)
        post(node['right'],now)
        now.append(root)
        return now
    return [pre(hi,[]),post(hi,[])]