import sys 
import math

input = sys.stdin.readline 

N = int(input())

# 한자리 소수
p  = [2, 3, 5, 7]

# 소수 판별
def prime(n):
  k = int(math.sqrt(n)) + 1
  for i in range(2, k):
    if n%i == 0:
      return False
  return True

def check(num):
  if len(str(num))==N:
    print(num)
    return

  for i in range(10):
    x = num * 10 + i
    if prime(x):
      check(x)
      
for i in p:
  check(i)