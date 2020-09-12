from test_script import timer
from typing import List
from functools import lru_cache


class Solution:
    @timer
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def tradeWindow(day: int, accountStatus: int, nowProfile: int):
            if day >= len(prices):
                return nowProfile
            if accountStatus == 0:
                return max(tradeWindow(day + 1, 1, nowProfile), tradeWindow(day + 1, 0, nowProfile))  # 买股票或者不买
            elif accountStatus == 1:
                nowProfile += prices[day] - prices[day - 1]
                return max(tradeWindow(day + 1, -1, nowProfile), tradeWindow(day + 1, 1, nowProfile))  # 卖股票或者不卖
            elif accountStatus == -1:
                return tradeWindow(day + 1, 0, nowProfile)

        return tradeWindow(0, 0, 0)


print(Solution().maxProfit([1, 2, 3, 0, 1]))
print(Solution().maxProfit([48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]))
