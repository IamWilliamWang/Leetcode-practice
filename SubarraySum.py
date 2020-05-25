from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrayCount = 0
        sum0ToN = defaultdict(int)  # key=前n项和，value=该前n项和出现了几次。构建完毕后索引信息会丢失但不重要
        sum0ToN[0] = 1  # 如果刚好是前n项和的话，sum-k==0
        sum = 0
        for num in nums:
            sum += num
            subarrayCount += sum0ToN[sum - k]
            sum0ToN[sum] += 1
        return subarrayCount


print(Solution().subarraySum([1], 0))
