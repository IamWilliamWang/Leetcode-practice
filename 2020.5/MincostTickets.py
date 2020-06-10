from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def searchDay(biggerThanWhichDay: int):
            for index in range(len(days)):
                if days[index] > biggerThanWhichDay:
                    return index
            return -1

        @lru_cache(maxsize=None)
        def minCost(daysStartIndex: int):
            if daysStartIndex == -1:
                return 0
            # 买1天的，买7天的，买30天的
            costList = [costs[0] + minCost(searchDay(days[daysStartIndex])),
                        costs[1] + minCost(searchDay(days[daysStartIndex] + 6)),
                        costs[2] + minCost(searchDay(days[daysStartIndex] + 29))]
            return min(costList)

        return minCost(0)


print(Solution().mincostTickets([1,4,6,7,8,20],[2,7,15]))
