# import sys

# input = sys.stdin.readline

# N = int(input())
# M = int(input())
# wrongs = []
# if M!=0 : wrongs = list(map(int,input().split()))

# cal = abs(N-100)
# print(cal)

# words = list(map(int,list(str(N))))
# print(words)
# add = 0

# def make_word(depth, word):
#     if depth == len(words):
#         return
#     make_word(depth+1,word)
# for w in words:
#     temp = w
#     plus = temp
#     minus = temp
#     while plus in wrongs:
#         plus+=1
#     while minus in wrongs:
#         minus+=1
#     print(temp)
#     add+=1
# print(add)