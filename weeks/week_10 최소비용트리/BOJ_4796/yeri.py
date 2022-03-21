"""
수학으로 품
"""
import sys
input=sys.stdin.readline

L,P,V=map(int,input().split())
num=1
while L!=0 and P!=0 and V!=0 :
    cnt=(V//P)*L + ( V%P if (V%P)<L else L)
    print("Case "+str(num)+": "+str(cnt))
    num+=1
    L, P, V = map(int, input().split())