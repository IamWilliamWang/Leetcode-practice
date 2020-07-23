from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        minLen = 2 ** 31 - 1
        sum = 0
        while j < len(nums):
            j += 1
            sum += nums[j - 1]
            while sum >= s:
                minLen = min(minLen, j - i)
                i += 1
                sum -= nums[i - 1]
        return minLen if minLen != 2 ** 31 - 1 else 0
