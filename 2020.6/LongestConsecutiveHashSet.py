from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        length, maxLength = 0, 0
        for num in nums:
            numsSet.add(num)
        for num in numsSet:
            if num - 1 not in numsSet:
                length = 0
                while num in numsSet:
                    length += 1
                    num += 1
                maxLength = max(maxLength, length)
        return maxLength


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
