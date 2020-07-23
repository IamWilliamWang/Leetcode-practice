from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = 2 ** 31 - 1
        minDistance = 2 ** 31 - 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                k = len(nums) - 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                if j != k and target - (nums[i] + nums[j] + nums[k]) < minDistance:
                    minDistance = target - (nums[i] + nums[j] + nums[k])
                    closestSum = nums[i] + nums[j] + nums[k]
                if k < len(nums) - 1 and nums[i] + nums[j] + nums[k + 1] - target < minDistance:
                    minDistance = (nums[i] + nums[j] + nums[k + 1]) - target
                    closestSum = nums[i] + nums[j] + nums[k + 1]
        return closestSum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest(
    nums=[0, 9, 5, 7, 8, 2, 3, 2, 1, 5, 3, 7, 1, 1, 0, 10, 6, 5, 7, 3, 5, 5, 4, 0, 2, 9, 1, 1, 5, 10, 7, 2, 10, 7, 7, 0, 5, 6, 6, 4, 9, 3, 0, 6, 10, 2, 6, 3, 7, 8, 3, 2, 6, 0, 9, 9, 7, 2, 8, 5, 6, 7, 9, 9, 8, 4, 5, 1, 7, 7, 1, 6, 6, 10, 5, 0, 5, 9, 4, 10, 5, 2, 8, 10, 1, 6, 0, 9, 3, 8, 7, 9, 0, 4, 1, 4, 10, 6, 1, 10], target=25))
