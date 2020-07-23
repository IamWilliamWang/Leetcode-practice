from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums)):
            j, k = 0, len(nums) - 1
            for j in range(i + 1, len(nums)):
                while j < k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] < target:
                    result += k - j
        return result
