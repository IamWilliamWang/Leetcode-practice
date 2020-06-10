from typing import List
from test_script import speedtest
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    def findDuplicate_fast(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return -1


import bisect

nums = list(range(100000))
bisect.insort_right(nums, 10000)
speedtest((Solution().findDuplicate, Solution().findDuplicate_fast), [nums])
