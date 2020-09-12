from functools import lru_cache
from typing import List
from test_script import speedtest
import numpy as np
import itertools
from collections import defaultdict

from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


class Solution:
    def twoSum_slow(self, n: int) -> List[float]:
        def runnable(prefix):
            ret = defaultdict(int)
            for dicesTuple in itertools.product(*dices):
                ret[sum(prefix) + sum(dicesTuple)] += 1
            return ret

        if n < 1:
            n = 1
        dices = [list(range(1, 7))] * (n - 1)
        counter = defaultdict(int)
        with ThreadPoolExecutor(max_workers=10) as pool:
            futures = list(pool.map(runnable, [twoElemTuple for twoElemTuple in itertools.product(list(range(1, 7)))]))
        for future in futures:
            for sumOfdices in future:
                counter[sumOfdices] += future[sumOfdices]
        sumOfAll = sum(counter.values())
        retList = []
        for sumOfTime in sorted(counter.keys()):
            retList.append(counter[sumOfTime] / sumOfAll)
        return retList

    @lru_cache(maxsize=None)
    def getCountAt(self, dice数量: int, dices点数和: int) -> int:
        if dice数量 < 1 or dices点数和 < dice数量 or dices点数和 > dice数量 * 6:
            return 0
        if dice数量 == 1:
            return 1
        ret = [self.getCountAt(dice数量 - 1, dices点数和 - i) for i in range(6, 0, -1)]
        return sum(ret)

    def twoSum(self, n: int) -> List[float]:
        dices点数和List = [self.getCountAt(n, sumOfdices) for sumOfdices in range(n, 6 * n + 1)]
        dices点数和Sum = sum(dices点数和List)
        return [dicesSum / dices点数和Sum for dicesSum in dices点数和List]


speedtest([Solution().twoSum, Solution().twoSum_slow], [10])
