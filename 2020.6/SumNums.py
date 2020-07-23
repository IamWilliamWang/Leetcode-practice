from itertools import accumulate


class Solution:
    def sumNums(self, n: int) -> int:
        # return list(accumulate(range(1, n + 1)))[-1]
        return sum(range(1, n + 1))
