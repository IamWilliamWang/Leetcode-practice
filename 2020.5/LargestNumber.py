from typing import List
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def searchPotentialResult(self, restMoney: int, choicesInt: int) -> None:
        if restMoney == 0:
            if choicesInt > self.maxResult:
                self.maxResult = choicesInt
        for i in range(len(self.cost)):
            if self.cost[i] == -1:
                continue
            if restMoney >= self.cost[i]:
                choice = int(i + 1)
                self.searchPotentialResult(restMoney - self.cost[i], choicesInt * 10 + choice)

    def largestNumber(self, cost: List[int], target: int) -> str:
        for i in range(len(cost)):
            for j in range(0, i):
                if cost[j] != -1 and cost[j] == cost[i]:
                    cost[j] = -1
        self.maxResult = -2 ** 31
        self.cost = cost
        self.searchPotentialResult(target, 0)
        return str(self.maxResult if self.maxResult != -2 ** 31 else 0)


print(Solution().largestNumber([70, 84, 55, 63, 74, 44, 27, 76, 34], 659))
