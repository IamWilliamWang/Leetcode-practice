from test_script import speedtest_format as speedtest
import numpy as np


class Solution:
    def new21Game_slow(self, N: int, K: int, W: int) -> float:
        limit爆点Inclusive, limit抽到点数为止Exclusive, max卡牌点数 = N, K, W
        array = np.zeros(limit抽到点数为止Exclusive + max卡牌点数)
        array[limit抽到点数为止Exclusive:limit爆点Inclusive + 1] = 1
        sums = array[limit抽到点数为止Exclusive + 1:limit抽到点数为止Exclusive + max卡牌点数].sum()
        for i in range(limit抽到点数为止Exclusive - 1, -1, -1):
            array[i] = array[i + 1:i + max卡牌点数 + 1].sum() / max卡牌点数
        return array[0]

    def new21Game(self, N: int, K: int, W: int) -> float:
        limit爆点Inclusive, limit抽到点数为止Exclusive, max卡牌点数 = N, K, W
        array = np.zeros(limit抽到点数为止Exclusive + max卡牌点数)
        array[limit抽到点数为止Exclusive:limit爆点Inclusive + 1] = 1
        sums = array[limit抽到点数为止Exclusive + 1:limit抽到点数为止Exclusive + max卡牌点数].sum()
        for i in range(limit抽到点数为止Exclusive - 1, -1, -1):
            sums += array[i + 1]
            array[i] = sums / max卡牌点数
            sums -= array[i + max卡牌点数]
        return array[0]


speedtest([Solution().new21Game, Solution().new21Game_slow], (10, 1, 10))
speedtest([Solution().new21Game, Solution().new21Game_slow], (6, 1, 10))
speedtest([Solution().new21Game, Solution().new21Game_slow], (21, 17, 10))
speedtest([Solution().new21Game, Solution().new21Game_slow], (7467, 6303, 1576))
speedtest([Solution().new21Game, Solution().new21Game_slow], (9811, 8776, 1096))
speedtest([Solution().new21Game, Solution().new21Game_slow], (7467, 6303, 1576))
