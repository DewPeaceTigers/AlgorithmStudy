def solution(n):
    answer = 0
    one=bin(n).count('1')
    for i in range(n+1,  1000001) :
        if bin(i).count('1')==one :
            return i