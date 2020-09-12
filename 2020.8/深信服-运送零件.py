#
#
# @param nums int整型一维数组
# @param m int整型
# @return int整型
#
from functools import reduce
from typing import List


def min_send(nums: List[int], m: int):
    queues=[[]for _ in range(m)]
    sumOfAll=sum(nums)
    for i in range(m):
        queues[i].append(nums.pop(0))
    def adjust(i:int):
        while len(queues[1])>1 and sum(queues[i-1])<sum(queues[i]):
            if sumOfAll/m-sum(queues[i][1:])>abs(sum(queues[i])-sumOfAll/m):
                break
            queues[i-1].append(queues[i].pop(0))
    while nums:
        queues[-1].append(nums.pop(0))
        for i in range(len(nums)-1,0,-1):
            adjust(i)
    return reduce(lambda x,y:max(sum(x),sum(y)),queues)
class Solution:
    def min_send(self, nums: List[int], m: int):
        minOfMaxes = 2 ** 31 - 1
        sumOfNums = sum(nums)

        def dist(n: int):
            return abs(n - sumOfNums / m)  # 当前和与最佳和之间的差距

        def dfs(i: int, nowMax: int):
            nonlocal minOfMaxes
            if i == len(nums):
                minOfMaxes = min(minOfMaxes, nowMax)
                return
            sectionSum = 0
            if i == m - 1:
                nowSum = sum(nums[i:])
                nowMax = max(nowMax, nowSum)
                minOfMaxes = min(minOfMaxes, nowMax)
                return
            while i < len(nums) and sectionSum < sumOfNums:
                sectionSum += nums[i]
                i += 1
            if sectionSum == nums[i - 1]:  # 只有一个元素时如果回退则会无限循环自己，没有选择的余地
                dfs(i, max(nowMax, sectionSum))
            else:
                if dist(sectionSum) < dist(sectionSum - nums[i - 1]):  # 不后退最佳
                    dfs(i, max(nowMax, sectionSum))
                else:  # 后退一步最佳
                    dfs(i - 1, max(nowMax, sectionSum - nums[i - 1]))  # 把超额的最后一个元素吐出来

        dfs(0, 0)
        return minOfMaxes


print(min_send([4, 3, 5, 10, 12], 2))
