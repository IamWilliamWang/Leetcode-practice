from functools import lru_cache

from test_script import speedtest


class Solution:
    @lru_cache(maxsize=None)
    def jumpFloorIIRecursive(self, number: int):
        if number == 1:
            return 1
        sum = 0
        for i in range(1, number):
            sum += self.jumpFloorIIRecursive(number - i)
        return sum + 1

    def jumpFloorIISlow(self, n):
        dp = [1]
        for i in range(1, n):
            dp.append(sum(dp) + 1)
        return dp[-1]

    def jumpFloorII(self, n):
        dp = [1]
        sum = 0
        for i in range(1, n):
            sum += dp[i - 1]
            dp.append(sum + 1)
        return dp[-1]


speedtest((Solution().jumpFloorIIRecursive, Solution().jumpFloorIISlow, Solution().jumpFloorII), [50])
