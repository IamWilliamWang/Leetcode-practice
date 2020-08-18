import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def isGood(start: int, stop: int) -> bool:
            for l in nums:
                if not any([True if start <= x < stop else False for x in l]):
                    return False
            else:
                return True

        resultBegin, resultStop, resultLen = 0, 0, 2 ** 31 - 1
        heap = []
        for l in nums:
            heap += l
        heapq.heapify(heap)
        selections = []
        i, j = heap[0], heap[0]
        while heap:
            smallNumber = heapq.heappop(heap)
            j = smallNumber + 1
            selections.append(smallNumber)
            while i < j and isGood(i, j):
                if j - i < resultLen:
                    resultBegin, resultStop, resultLen = i, j, j - i
                i = selections.pop(0) if selections else i + 1
        return [resultBegin, resultStop - 1]  # 因为我用的exclusive


print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
