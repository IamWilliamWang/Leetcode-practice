from functools import lru_cache


class Solution:
    def rob(self, nums: list) -> int:
        # @lru_cache(maxsize=None)
        # def dp(index: int) -> int:
        #     if index is 0:
        #         return nums[index]
        #     elif index is 1:
        #         return max(nums[0], nums[1])
        #     return max(dp(index-1), dp(index-2) + nums[index])
        # return dp(len(nums)-1)
        array = []
        numsLen = len(nums)
        if numsLen >= 1:
            array.append(nums[0])
        if numsLen >= 2:
            array.append(max(nums[0], nums[1]))
        for index in range(2, numsLen):
            array.append(max(array[index - 1], array[index - 2] + nums[index]))
        return array[-1] if array != [] else 0
