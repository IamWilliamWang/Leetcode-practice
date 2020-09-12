import sys
from collections import Counter, defaultdict

# for round in range(int(sys.stdin.readline().strip())):
#     N = int(sys.stdin.readline().strip())
#     values = list(map(int, sys.stdin.readline().strip().split()))[:N]  # 暂时假定为int
#     valuesDict = Counter(values)
#     minResult = 2 ** 31 - 1
#
#
#     def dp(usedDict: defaultdict, firstHave: int, secondHave: int):
#         global minResult
#         restDict = valuesDict.copy()
#         for used in usedDict:
#             restDict[used] -= usedDict[used]
#         if not restDict:
#             return
#         if firstHave == secondHave:
#             restValueSum = 0
#             for rest in restDict:
#                 restValueSum += restDict[rest] * rest
#             minResult = min(minResult, restValueSum)
#         for value in restDict:
#             if restDict[value] == 0:
#                 continue
#             tmp = usedDict.copy()
#             tmp[value] += 1
#             dp(tmp, firstHave + value, secondHave)  # 把i给了第一个
#             dp(tmp, firstHave, secondHave + value)  # 把i给了第二个
#
#
#     dp(defaultdict(int), 0, 0)
#     print(minResult)
from functools import lru_cache
import sys


def main():
    for round in range(int(sys.stdin.readline().strip())):
        N = int(sys.stdin.readline().strip())
        values = list(map(int, sys.stdin.readline().strip().split()))[:N]  # 暂时假定为int
        minResult = 2 ** 31 - 1
        visitedIdxSet = set()

        @lru_cache(maxsize=None)
        def dp(firstHave: int, secondHave: int):
            nonlocal minResult
            nonVisitedIdxSet = set(range(len(values))).difference(visitedIdxSet)
            nonVisitedList = list(values[idx] for idx in nonVisitedIdxSet)
            if firstHave == secondHave:
                minResult = min(minResult, sum(nonVisitedList))
            if len(visitedIdxSet) == len(values):
                return
            for nowIdx in nonVisitedIdxSet:
                value = values[nowIdx]
                visitedIdxSet.add(nowIdx)
                dp(firstHave + value, secondHave)
                dp(firstHave, secondHave + value)
                visitedIdxSet.remove(nowIdx)

        dp(0, 0)
        print(minResult)

if __name__ == "__main__":
    main()
