from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        摩尔投票法的实现（不适用于求出现次数小于等于一半的众数，如[1, 2, 3, 2, 3, 2, 3, 2]）
        :param nums:
        :return:
        """
        survivor = -1  # 占领的国家
        survivorCount = 0  # 占领的士兵数量
        for num in nums:  # 多国混战
            if not survivorCount:  # 没有其他国家的士兵
                survivor, survivorCount = num, 1  # 占领城池
            else:
                survivorCount = survivorCount + 1 if survivor == num else survivorCount - 1  # 攻城
        return survivor  # 最后占领国


print(Solution().majorityElement([1, 2, 3, 2, 3, 2, 3, 2]))
