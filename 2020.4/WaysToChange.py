import numpy as np
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def recursion(self,coinCount1:int, coinCount2:int, coinCount3:int, coinCount4:int):
        self.count += 1
        coins=[coinCount1,coinCount2,coinCount3,coinCount4]
        if (np.array(coins)>=0).all() is False:
            return 0
        return self.recursion(coins+[-1,2,1,0])+self.recursion()
    def waysToChange(self, n: int) -> int:
        硬币面值 = [25, 10, 5, 1]
        初始硬币数 = [0, 0, 0, 0]
        for i in range(len(硬币面值)):
            while n >= 硬币面值[i]:
                n -= 硬币面值[i]
                初始硬币数[i] += 1
        self.count=0




        # def 变一位有多少种(coin: int):
        #     if coin == 5:
        #         return 1
        #     if coin == 10:
        #         return 1 + 2 * 变一位有多少种(5)
        #     if coin == 25:
        #         return 1 + 2 * 变一位有多少种(10) + 1 * 变一位有多少种(5)
        # if n == 0:
        #     return 0
        # 面值对应的次数 = [8, 3, 1, 0]
        # 硬币面值 = [25, 10, 5, 1]
        # count = 1
        # 初始硬币数 = [0, 0, 0, 0]
        # for i in range(len(硬币面值)):
        #     while n >= 硬币面值[i]:
        #         n -= 硬币面值[i]
        #         初始硬币数[i] += 1
        #     count += 初始硬币数[i] * 面值对应的次数[i]
        # return count


print(Solution().waysToChange(15))
