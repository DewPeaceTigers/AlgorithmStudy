N = 10 * 3

class Node:
    delete = False

    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None


def solution(n, k, cmd):
    answer = ''
    global N
    N = n
    now = k
    stack = []  # 삭제된 행
    table = []
    for i in range(n):
        table.append(Node(i - 1, i + 1))

    print(table[7].next)
    for c in cmd:
        print("now : " + str(now))
        if c[0] == "C": #삭제
            table[now].delete = True
            stack.append(now)

            #삭제된 위아래 행 연결
            prev, next = table[now].prev, table[now].next

            if prev != None:
                table[prev].next = next

            if next != None:
                table[next].prev = prev

            #커서값 수정
            if next != None:
                now = next
            else:
                now = prev

        elif c[0] == "Z": #복구
            tmp = stack.pop() #가장 최근 삭제행
            print("tmp : " + str(tmp))
            table[tmp].delete = False

            #복구된 행의 위아래 행 연결
            prev, next = table[tmp].prev, table[tmp].next

            if prev != None:
                table[prev].next = tmp

            if next != None:
                table[next].prev = tmp
        else: #커서 이동
            command, num = c.split()
            if command == "D":
                for _ in range(int(num)):
                    now = table[now].next
            else:
                for _ in range(int(num)):
                    now = table[now].prev


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])