N=int(input())
nums = list(map(int,input().split()))
count=0
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for n in nums:
    if isPrime(n): count += 1
print(count)