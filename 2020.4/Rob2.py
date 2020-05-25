class Solution:
    def rob(self, nums: list) -> int:
        # def dp(l: List[int], index: int) -> int:
        #     if index is 0:
        #         return l[0]
        #     if index is 1:
        #         return max(l[0], l[1])
        #     return max(dp(l, index - 2) + l[index], dp(l, index - 1))
        # return max(dp(nums[:-1], len(nums) - 2), dp(nums[1:], len(nums) - 2))
        def dp(numList: list):
            array = []
            numsLen = len(numList)
            if numsLen >= 1:
                array.append(numList[0])
            if numsLen >= 2:
                array.append(max(numList[0], numList[1]))
            for index in range(2, numsLen):
                array.append(max(array[index - 1], array[index - 2] + numList[index]))
            return array[-1] if array != [] else 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:-1]))
