from collections import defaultdict
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, winnerTimes = -1, 0
        maxValue = max(arr)
        while True:
            if arr[0] < arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            if arr[0] == winner:
                winnerTimes += 1
            else:
                winner, winnerTimes = arr[0], 1
            if winnerTimes == k or arr[0] == maxValue:
                break
            arr.append(arr.pop(1))
        return winner


print(Solution().getWinner(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000))
