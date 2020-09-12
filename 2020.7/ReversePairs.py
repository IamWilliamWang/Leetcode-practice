from typing import List
from test_script import speedtest

from concurrent.futures.thread import ThreadPoolExecutor
from asyncio import as_completed
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # def smallerCount(startIdx):
        #     return len([secondIdx for secondIdx in range(startIdx + 1, len(nums)) if nums[startIdx] > nums[secondIdx]])
        #
        # futures = []
        # with ThreadPoolExecutor(max_workers=64) as pool:
        #     for i in range(len(nums) - 1):
        #         futures.append(pool.submit(smallerCount, i))
        #     pool.shutdown()
        # result = 0
        # for future in futures:
        #     result += future.result()
        # return result
        ans = 0
        table = []
        for num in nums:
            insertIndex = bisect.bisect(table, num)  # 找到num的插入位置（也就是第一个大于num的位置）
            table.insert(insertIndex, num)
            ans += len(table) - insertIndex - 1  # 算出比num大的有多少个
        return ans


# speedtest((Solution().reversePairs, lambda x: 0), [[1]])
speedtest((Solution().reversePairs, lambda x: 5), [[7, 5, 6, 4]])
import LongLongCase
speedtest((Solution().reversePairs, lambda x: 624875572),[LongLongCase.long_long_case1()])
