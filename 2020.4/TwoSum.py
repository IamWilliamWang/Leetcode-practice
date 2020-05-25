class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        import numpy as np
        nums = np.array(nums)
        numsMin = nums.min()
        if numsMin < 0:
            target -= numsMin * 2
            nums -= numsMin
        maxIndex = 0
        for maxIndex in range(len(nums) - 1, 0, -1):
            if nums[maxIndex] <= target:
                break
        for i in range(maxIndex, 0, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] + nums[j] == target:
                    return [j, i]
        return []


print(Solution().twoSum([-3, 4, 3, 90], 0))
