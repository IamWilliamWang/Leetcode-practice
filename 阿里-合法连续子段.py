# 合法连续子段
import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().strip().split())
line = sys.stdin.readline().strip()
a = list(map(int, line.split()))
if len(a) > n:
    a = a[:n]
array, arrayLen, repeatMinTimes = a, n, m
i, j = 0, 0
counter = defaultdict(int)
ans = 0
while j < arrayLen:
    while j < arrayLen and (len(counter) == 0 or max(counter.values()) < repeatMinTimes):
        counter[array[j]] += 1
        j += 1
    if j >= arrayLen:
        break
    # for tmp in range(j - 1, arrayLen):
    #     print('[%d,%d]' % (i + 1, tmp + 1))
    ans += arrayLen - (j - 1)
    counter[array[i]] -= 1
    i += 1
print(ans)
