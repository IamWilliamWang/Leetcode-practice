import sys
import math
from functools import lru_cache

@lru_cache(maxsize=None)
def getPossibilities(a: int, b: int):
    global potentialCounts
    restLen = targetLen - songALen * a - songBLen * b
    if restLen == 0:
        if a <= songACount and b <= songBCount and (a, b) not in potentialCounts:
            potentialCounts += [(a, b)]
        return
    if restLen < 0:
        return
    getPossibilities(a + 1, b)
    getPossibilities(a, b + 1)

def permutation(high: int, low: int):
    return math.factorial(high) // math.factorial(high - low)
def combination(high:int,low:int):
    return permutation(high,low)//math.factorial(low)

targetLen = int(sys.stdin.readline().strip())
songACount, songALen, songBCount, songBLen = [0] * 4
songALen, songACount, songBLen, songBCount = list(map(int, sys.stdin.readline().strip().split()))
potentialCounts = []
getPossibilities(0, 0)
result = 0
for A和B长度分别有几首 in potentialCounts:
    歌单拥有的歌数 = sum(A和B长度分别有几首)
    # result += combination(歌单拥有的歌数, A和B长度分别有几首[0]) * (permutation(songACount, A和B长度分别有几首[0]) * permutation(songBCount, A和B长度分别有几首[1]))
    result += combination(songACount, A和B长度分别有几首[0]) * combination(songBCount, A和B长度分别有几首[1])
print(result % 1000000007)
