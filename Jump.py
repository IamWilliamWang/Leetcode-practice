from typing import List
from functools import lru_cache
from test_script import timer


class Solution:
    @timer
    def jump_recursive(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i: int):
            if i == len(nums) - 1:
                return 0
            elif i >= len(nums):
                return -1
            resultList = []
            for step in range(nums[i], 0, -1):
                ret = dp(i + step)
                if ret != -1:
                    resultList.append(1 + ret)
            return min(resultList) if resultList else -1

        if not nums:
            return 0
        return dp(0)

    @timer
    def jump_iteration(self, nums: List[int]) -> int:
        if not nums:
            return 0
        jumpList = [-1] * len(nums)
        jumpList[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            ans = []
            for step in range(nums[i], 0, -1):
                if i + step < len(nums) and jumpList[i + step] != -1:
                    ans.append(jumpList[i + step])
            jumpList[i] = 1 + min(ans) if ans else -1
        return jumpList[0]

    def jump(self, nums: List[int]) -> int:
        times = 0
        jumpEndPerStep = 0
        maxPosition = 0
        for i in range(len(nums)):
            maxPosition = max(i + nums[i], maxPosition)  # 刷新下一步最大地点
            if i == jumpEndPerStep:  # 到达跳跃结束点
                jumpEndPerStep = maxPosition  # 跳到下一步地点，不是从i跳到maxPosition，是从最好的位置跳到maxPosition达到局部最优
                times += 1
        return times


print(Solution().jump([2, 3, 1, 1, 4]))
