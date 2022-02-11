import sys
input = sys.stdin.readline

# L, C (3 ≤ L ≤ C ≤ 15) 입력
L, C = map(int, input().split())

# 모음 문자 리스트
vowel =['a','e','i','o','u']

# 문자 입력
alpha = input().split()
alpha.sort()

idx=[]
pw='' # 암호 문자열 저장
cnt=[0,0] # 자음, 모음 개수 저장

def dfs(i, l, c):
  global pw

  if len(idx)==L:
    # 자음 두개 이상, 모음 한개 이상
    if cnt[0]>=2 and cnt[1]>=1:
      print(pw)
    return
  
  for i in range(i, c):
    isVowel=0
    if i not in idx:
      idx.append(i)
      pw+= alpha[i]
      if alpha[i] in vowel: 
        isVowel=1
      cnt[isVowel]+=1

      # 정렬된 문자 -> i+1 대입
      dfs(i+1, l, c)

      idx.pop() 
      pw = pw[:-1]
      cnt[isVowel]-=1

dfs(0, L, C)