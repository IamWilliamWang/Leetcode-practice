#
# calculate correct encode number
# @param length int整型 encode string length
# @return int整型
#
from functools import reduce
from math import sqrt

from test_script import Prime

PRIME = Prime()


class Solution:
    def get质数因子(self, n: int):
        result = []
        for i in range(2, int(sqrt(n)) + 1):
            if n // i * i == n:
                if i in PRIME:
                    result.append(i)
                if n // i in PRIME:
                    result.append(n // i)
        return set(result)

    def calEncodeNumber(self, length: int):
        mulArray = [1]
        for i in range(2, length + 1):
            if i in PRIME:
                mulArray.append(2)
            else:
                tmp = self.get质数因子(i)
                mulArray.append(1 + 2 ** -len(tmp))
        return int(reduce(lambda x, y: x * y, mulArray)) % 1000000369


print(Solution().calEncodeNumber(4))
