'''
전위순회 루-왼-오
후위순회 왼-오-루
'''
import sys

sys.setrecursionlimit(10000)

class Node(object) :
    def __init__(self, info):
        self.num=info[2]
        self.pos=info[:2]
        self.left=None
        self.right=None

def set_node(tree, info) :
    if tree.pos[0]>info[0] :
        if tree.left :
            set_node(tree.left, info)
        else:
            tree.left=Node(info)
    else:
        if tree.right:
            set_node(tree.right, info)
        else:
            tree.right=Node(info)

def pre_order(tree) :
    path=[tree.num]
    if tree.left:
        path+=pre_order(tree.left)
    if tree.right:
        path+=pre_order(tree.right)

    return path

def post_order(tree) :
    path=[]
    if tree.left:
        path += post_order(tree.left)
    if tree.right:
        path += post_order(tree.right)

    path.append(tree.num)
    return path

def solution(nodeinfo):
    for i in range(len(nodeinfo)) : #노드번호 추가
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x:(-x[1], x[0])) #level이 높은 순으로 정렬

    tree=Node(nodeinfo[0])
    for info in nodeinfo[1:] :
        set_node(tree, info)

    return [pre_order(tree), post_order(tree)]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))