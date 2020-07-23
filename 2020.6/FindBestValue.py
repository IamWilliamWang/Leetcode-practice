from typing import List

from test_script import speedtest


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0
        arr.sort()
        sum = 0  # 保存arr[0,i)的和
        i = 0
        while i < len(arr):  # 用for会错过i==len(arr)的情况
            if sum + (len(arr) - i) * arr[i] > target:  # 如果把arr[i...]全变成arr[i]的和，大于target就结束
                break
            sum += arr[i]
            i += 1
        if i == len(arr):  # 如果target太大了，返回最后一个数字
            return arr[-1]
        if i == 0:  # 如果target太小了，所有数字都要变化。计算范围
            potentialResultRange = target // len(arr), target // len(arr) + 1
        else:  # 在arr[i-1]到arr[i]中都有可能
            potentialResultRange = [arr[i - 1], arr[i]]
        minDistance = 2 ** 31 - 1  # 与target最小差
        result = arr[-1]
        for potentialResult in range(potentialResultRange[0], potentialResultRange[1] + 1):  # arr[i-1]到arr[i]中挨个试一遍
            if abs((sum + (len(arr) - i) * potentialResult) - target) < minDistance:  # 刷新最好的结果
                minDistance = abs(sum + (len(arr) - i) * potentialResult - target)
                result = potentialResult
        return result


speedtest([Solution().findBestValue, lambda x, y: 3], ([4, 9, 3], 10))
speedtest([Solution().findBestValue, lambda x, y: 5], ([2, 3, 5], 10))
speedtest([Solution().findBestValue, lambda x, y: 11361], ([60864, 25176, 27249, 21296, 20204], 56803))
