from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []
        for candy in candies:
            result.append(True if candy + extraCandies >= maxCandy else False)
        return result
