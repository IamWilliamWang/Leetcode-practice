from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stackOfIndex = []
        result = [0] * len(T)
        for i, temperature in enumerate(T):
            while stackOfIndex and T[stackOfIndex[-1]] < temperature:
                j = stackOfIndex.pop()
                result[j] = i - j
            stackOfIndex += [i]
        return result
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))