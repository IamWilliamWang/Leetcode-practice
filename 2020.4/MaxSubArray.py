class Solution:
    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return -2147483648
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(max(sums[i - 1] + nums[i],nums[i]))
        return max(sums)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
