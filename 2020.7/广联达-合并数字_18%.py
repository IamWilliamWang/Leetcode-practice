import sys
from collections import defaultdict

n = int(input().strip())
arr = list(map(int, input().strip().split()))[:n]
# arr = [3, 5, 7, 2, 6, 7, 9, 8, 8, 1, 2, 6, 10, 10, 1, 2, 8, 7, 5, 0, 8, 4, 6, 8, 5, 2, 7, 7, 2, 2, 5, 5, 8, 6, 10, 1, 2, 6, 5, 2, 1, 10, 6, 9, 10, 6, 3, 2, 2, 2, 0, 10, 4, 6, 4, 1, 0, 6, 0, 2, 9, 8, 0, 2, 4, 9, 0, 2, 10, 8, 0, 6, 8, 10, 7, 7, 4, 6, 1, 8, 4, 5, 10, 10, 3, 5, 8, 0, 6, 7, 4, 1, 6, 7, 2, 5, 1, 10, 0, 9]
while True:
    nowCounter = defaultdict(int)
    nowCounterIndex = defaultdict(list)
    for i, x in enumerate(arr):
        nowCounter[x] += 1
        nowCounterIndex[x].append(i)
    if list(nowCounter.values()) == [1] * len(nowCounter):
        break
    for key in sorted(nowCounter.keys()):
        if nowCounter[key] > 1:
            del arr[nowCounterIndex[key][1]]
            arr[nowCounterIndex[key][0]] *= 2
            break
sys.stdout.write(' '.join(map(str, arr)))
