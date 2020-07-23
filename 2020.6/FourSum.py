from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len(nums) - 1
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    while k < l and nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    if k == l:
                        break
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result += [[nums[i], nums[j], nums[k], nums[l]]]
        return result
