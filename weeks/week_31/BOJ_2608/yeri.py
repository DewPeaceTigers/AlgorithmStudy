import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,
       'XC':90,'CD':400,'CM':900}
def decode(s):
    num = 0
    idx = 0
    while idx<len(s):
        if idx == len(s) - 1:
            num += dic[s[idx]]
        elif s[idx:idx + 2] in dic:
            num += dic[s[idx:idx + 2]]
            idx += 1
        else:
            num += dic[s[idx]]
        idx+=1
    return num

num = decode(A)+decode(B)
print(num)

def encode(num):
    string = ""
    dic_items = list(dic.items())
    dic_items.sort(key=lambda x:-x[1])
    while num>0:
        for code, n in dic_items:
            if num >= n:
                string += code
                num-=n
                break
    return string

print(encode(num))