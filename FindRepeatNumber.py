from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            if num in numbers:
                return num
            numbers.add(num)
        return -1
