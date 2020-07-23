from typing import List

from test_script import timer


class Solution:
    @timer
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        # dpSet = {shorter, longer}
        # for i in range(1, k):
        #     newSet = set()
        #     for length in dpSet:
        #         newSet.add(length + shorter)
        #         newSet.add(length + longer)
        #     dpSet = newSet
        # return list(dpSet)
        return [shorter * k + (longer - shorter) * i for i in range(k + 1)]


print(Solution().divingBoard(7, 3625, 19808))
