'''
전위순회는 루-왼-오
후위순회는 왼-오-루

'''
import sys
sys.setrecursionlimit(10000)

class Node(object) :
    def __init__(self, info):
        self.num=info[2]
        self.pos=info[:2]
        self.left=None
        self.right=None

def solution(nodeinfo):
    for i in range(len(nodeinfo)) : #노드번호 저장
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x:(-x[1], x[0]))

    tree=Node(nodeinfo[0])
    for info in nodeinfo[1:]:
        set_node(tree, info)

    return [preorder(tree), postorder(tree)]

def set_node(root, info) :
    if root.pos[0]>info[0] :
        if root.left:
            set_node(root.left, info)
        else:
            root.left=Node(info)
    else:
        if root.right:
            set_node(root.right, info)
        else:
            root.right=Node(info)

def postorder(tree):
    path=[]
    if tree.left:
        path+=postorder(tree.left)
    if tree.right:
        path+=postorder(tree.right)
    path.append(tree.num)
    return path
def preorder(tree) :
    path=[tree.num]
    if tree.left:
        path+=preorder(tree.left)
    if tree.right:
        path+=preorder(tree.right)
    return path

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))