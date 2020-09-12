import math
from functools import lru_cache


@lru_cache(maxsize=None)
def dp(i: int, sumOfAll: int):
    global result
    if i == N - 2:
        sumOfAll %= 3
        arange = [math.ceil((down + sumOfAll) / 3), up]
        result += (arange[1] - arange[0]) // 3 + 1
    else:
        for nextNum in range(down, up + 1):
            dp(i + 1, sumOfAll + nextNum)


N, down, up = list(map(int, input().strip().split()))
result = 0
for first in range(down, up + 1):
    dp(0, first)
print(result % (int(10e9) + 7))
