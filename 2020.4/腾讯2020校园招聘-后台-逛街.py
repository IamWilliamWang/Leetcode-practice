import sys
n = int(sys.stdin.readline().strip())
heights = list(map(int, sys.stdin.readline().strip().split()))
if len(heights) > n:
    heights = heights[:n]
result = [1] * n
for i in range(n):
    left, right = 0, 0
    # look right
    maxLimit = 0
    for j in range(i+1, n):
        if heights[j] > maxLimit:
            maxLimit = heights[j]
            right += 1
    # look left
    maxLimit = 0
    for j in range(i-1, -1, -1):
        if heights[j] > maxLimit:
            maxLimit = heights[j]
            left += 1
    result[i] += left + right
print(' '.join(list(map(str, result))))
