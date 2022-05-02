n, k = map(int, input().split())
items = list(map(int, input().split()))
tap = []
ans = 0

for i, item in enumerate(items):
    if item in tap:
        continue
    if len(tap) < n:
        tap.append(item)
    else:
        val = 0
        idx = -1
        ans += 1
        tmp = items[i:]
        for x in tap:
          if x in tmp:
            target = tmp.index(x)
            if idx < target:
              idx = target
              val = x
          else:
              val = x
              break
        tap[tap.index(val)] = item

print(ans)