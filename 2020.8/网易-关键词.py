import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
words = defaultdict(int)
for _ in range(N):
    words[input().strip()] += 1
ans = 0
for word in words:
    time = words[word]
    if time / N >= 0.01:
        ans += 1
print(ans)
