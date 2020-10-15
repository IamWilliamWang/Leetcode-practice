from typing import List
from heapq import heapify, heapreplace


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return []
        result = [-x for x in arr[:k]]
        heapify(result)
        for i in range(k, len(arr)):
            if arr[i] < -result[0]:
                heapreplace(result, -arr[i])
        return [-x for x in result]
