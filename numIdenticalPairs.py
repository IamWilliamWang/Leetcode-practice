from test_script import speedtest
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


speedtest((Solution().numIdenticalPairs, lambda x: 4), [[1, 2, 3, 1, 1, 3]])
speedtest((Solution().numIdenticalPairs, lambda x: 6), [[1, 1, 1, 1]])
speedtest((Solution().numIdenticalPairs, lambda x: 0), [[1, 2, 3]])
