from typing import List
import heapq


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        heapq.heapify(nums)
        while nums and nums[0] <= 0:
            heapq.heappop(nums)
        shouldBe = 1
        while nums:
            if shouldBe < nums[0]:
                return shouldBe
            if shouldBe == nums[0]:
                shouldBe += 1
            heapq.heappop(nums)
        return shouldBe


print(Solution().firstMissingPositive([0, 2, 2, 1, 1]))
