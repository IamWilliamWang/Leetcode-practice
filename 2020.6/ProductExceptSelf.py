from typing import List
from test_script import speedtest_format as speedtest
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        zeroCount = nums.count(0)
        if zeroCount > 1:
            return [0] * len(nums)
        elif zeroCount == 1:
            result = [0] * len(nums)
            result[nums.index(0)] = reduce(lambda x, y: x * y, [num for num in nums if num], 1)
            return result
        multipliesList = []
        multiplies = 1
        for num in nums:
            multiplies *= num
            multipliesList.append(multiplies)
        result = []
        for i in range(len(nums)):
            result.append((multipliesList[i - 1] if i > 0 else 1) * (multipliesList[-1] // multipliesList[i]))
        return result

    def productExceptSelf_withoutMultiply(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        multiSum = 1
        leftMultipliesList = []
        rightMultipliesList = []
        for num in nums:
            multiSum *= num
            leftMultipliesList += [multiSum]
        multiSum = 1
        for num in reversed(nums):
            multiSum *= num
            rightMultipliesList += [multiSum]
        rightMultipliesList = rightMultipliesList[::-1]
        result = []
        for i in range(len(nums)):
            result += [
                (leftMultipliesList[i - 1] if i > 0 else 1) * (rightMultipliesList[i + 1] if i < len(nums) - 1 else 1)]
        return result


speedtest([Solution().productExceptSelf, Solution().productExceptSelf_withoutMultiply], [[0]])
speedtest([Solution().productExceptSelf, Solution().productExceptSelf_withoutMultiply], [[0, 0]])
speedtest([Solution().productExceptSelf, Solution().productExceptSelf_withoutMultiply], [[1, 2, 3, 4]])
speedtest([Solution().productExceptSelf, Solution().productExceptSelf_withoutMultiply], [list(range(10000))])
