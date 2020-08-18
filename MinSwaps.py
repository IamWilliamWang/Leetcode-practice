from typing import List

from test_script import speedtest


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        lastZeros = []
        for row in grid:
            lastZeroCount = 0
            while lastZeroCount < len(row) and row[-1 - lastZeroCount] == 0:
                lastZeroCount += 1
            lastZeros.append(lastZeroCount)
        moveToRowIdx = [max(0, len(grid) - 1 - zero) for zero in lastZeros]
        ans = 0
        # 冒泡排序
        # for i in range(len(moveToRowIdx)):
        #     for j in range(len(moveToRowIdx) - i - 1):
        #         if moveToRowIdx[j] > j and moveToRowIdx[j]!=moveToRowIdx[j+1]:
        #             moveToRowIdx[j], moveToRowIdx[j + 1] = moveToRowIdx[j + 1], moveToRowIdx[j]
        #             ans += 1
        for row in range(len(moveToRowIdx)):
            goodIdx = row
            while goodIdx < len(moveToRowIdx) and not moveToRowIdx[goodIdx] <= row:
                goodIdx += 1
            if goodIdx == len(moveToRowIdx):
                return -1
            ans += goodIdx - row
            moveToRowIdx.insert(row, moveToRowIdx.pop(goodIdx))
        else:
            return ans


speedtest([Solution().minSwaps, lambda *args: 3], [[[0, 0, 1], [1, 1, 0], [1, 0, 0]]])
speedtest([Solution().minSwaps, lambda *args: -1], [[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]])
speedtest([Solution().minSwaps, lambda *args: 0], [[[1, 0, 0], [1, 1, 0], [1, 1, 1]]])
speedtest([Solution().minSwaps, lambda *args: 4],
          [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]]])
speedtest([Solution().minSwaps, lambda *args: 0], [[[0, 0], [0, 1]]])
speedtest([Solution().minSwaps, lambda *args: 6],
          [[[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]]])
speedtest([Solution().minSwaps, lambda *args: -1], [[[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0]]])
speedtest([Solution().minSwaps, lambda *args: 2], [
    [[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0]]])
