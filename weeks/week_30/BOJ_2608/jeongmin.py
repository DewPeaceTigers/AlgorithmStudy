import sys

input = sys.stdin.readline

r1 = input().rstrip()
r2 = input().rstrip()

roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
smallLarge = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

total = list(roman.items())
total.extend(list(smallLarge.items()))
total.sort(key=lambda x:-x[1])


def romanToArabic(r):
    n = 0

    for key in smallLarge.keys():
        if key in r:
            r = r.replace(key, "")
            n += smallLarge[key]

    # 나머지 로마숫자 더하기
    for x in r:
        n+= roman[x]

    return n


def arabicToRoman(n):
    r = ""
    while n>0:
        for code, num in total:
            if n >= num:
                r += code
                n -= num
                break
    return r


sum_result = romanToArabic(r1) + romanToArabic(r2)
print(sum_result)  # 두 수를 더한 값
print(arabicToRoman(sum_result))