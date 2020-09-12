from collections import defaultdict
import sys

n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))[:n]
stack = []
blacklist = set()
counter = defaultdict(int)
for num in arr:
    if counter[num] > m - 1:
        blacklist.add(num)
        while stack and stack[-1] == num:
            stack.pop()
    if num not in blacklist:
        stack.append(num)
        counter[num] += 1
sys.stdout.write(' '.join(map(str, stack)))
