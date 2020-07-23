from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxPlus = 0
        result = 0
        for i, num in enumerate(A):
            result = max(result, maxPlus + num - i)
            maxPlus = max(maxPlus, num + i)
        return result
