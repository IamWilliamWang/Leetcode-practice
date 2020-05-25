from functools import lru_cache


class Solution:
    def canJump(self, nums: list) -> bool:
        if nums == []:
            return False
        @lru_cache(maxsize=None)
        def find(index: int) -> bool:
            """
            寻找该位置出发有没有可能到达终点
            :param index: 当前位置
            :return:
            """
            if index >= len(nums):
                return False
            if index == len(nums) - 1:
                return True
            for step in range(nums[index], 0, -1):
                if find(index + step):
                    return True
            return False
        # 先看看每次以最大步伐向前进，有没有跨过终点
        i = 0
        while nums[i] > 0:  # 如果碰到0就跳出
            i += nums[i]
            if i >= len(nums):  # 如果跨过了终点，证明可能有解
                return find(0)  # 求解
            if i == len(nums) - 1:  # 如果刚好踩在终点了，完美
                return True
        return False


print(Solution().canJump(
    [1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0]))
