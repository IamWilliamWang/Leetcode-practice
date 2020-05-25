from typing import List
from functools import lru_cache


class Solution:
    def maxProduct_noDP(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def multiplySum(startIndex: int, endIndex: int) -> int:
            if startIndex >= endIndex:
                return 0
            result = 1
            for i in range(startIndex, endIndex):
                result *= nums[i]
            return result

        negNumIndexList = []
        zeroNumIndexList = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negNumIndexList.append(i)
            elif nums[i] == 0:
                zeroNumIndexList.append(i)
        if len(negNumIndexList) == 0:
            if not zeroNumIndexList:
                return multiplySum(0, len(nums))
            maxMul = 0
            detectList = [-1] + zeroNumIndexList + [len(nums)]
            for i in range(1, len(detectList) - 1):
                former = multiplySum(detectList[i - 1] + 1, detectList[i])
                later = multiplySum(detectList[i] + 1, detectList[i + 1])
                maxMul = max(maxMul, former, later)
            return maxMul
        if len(negNumIndexList) == 1:
            if len(nums) > 1:
                return max(multiplySum(0, negNumIndexList[0]), multiplySum(negNumIndexList[0] + 1, len(nums)))
            return nums[0]
        maxMul = 0
        for indexInNegNumberIndexList1 in range(len(negNumIndexList)):
            for indexInNegNumberIndexList2 in range(indexInNegNumberIndexList1 + 1, len(negNumIndexList), 2):
                fromIndexInNums = negNumIndexList[indexInNegNumberIndexList1 - 1] + 1 if indexInNegNumberIndexList1 > 0 else \
                    negNumIndexList[indexInNegNumberIndexList1]
                toIndexInNums = negNumIndexList[indexInNegNumberIndexList2 + 1] if indexInNegNumberIndexList2 < len(
                    negNumIndexList) - 1 else negNumIndexList[indexInNegNumberIndexList2] + 1
                maxMul = max(maxMul, multiplySum(fromIndexInNums, toIndexInNums))
        return maxMul

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = -2 ** 31  # 保存最大的结果
        maxMul = minMul = 1  # 临时最大，最小初始化
        for i in range(len(nums)):
            if nums[i] < 0:  # 如果当前是负数，证明最大和最小该颠倒了
                maxMul, minMul = minMul, maxMul
            maxMul = max(nums[i], maxMul * nums[i])  # max(当前数字, 上一步的局部最大*当前数字)，保证局部最大
            minMul = min(nums[i], minMul * nums[i])  # min(当前数字, 上一步的局部最小*当前数字)，保证局部最小
            result = max(result, maxMul)  # 保存结果
        return result


print(Solution().maxProduct([1, 3, 0, 0, 2]))
